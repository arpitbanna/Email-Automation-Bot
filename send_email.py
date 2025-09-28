"""
📧 Email Automation Bot
Author: SllHex
Description:
A clean, professional Python script to send automated emails to a list of recipients.
It reads recipients from a CSV file, uses config.json for settings, and logs
success/failure for each email to a CSV log file.
"""

import smtplib
import csv
import json
import time
from datetime import datetime

# -----------------------------
# Configuration
CONFIG_FILE = "config.json"
EMAILS_FILE = "emails.csv"
LOG_FILE = "sent_log.csv"
RETRIES = 2
DELAY_SECONDS = 1.0   # Delay between sending emails (seconds)

# -----------------------------
# Functions

def load_config(path=CONFIG_FILE):
    """Load configuration from JSON file."""
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)

def read_recipients(path=EMAILS_FILE):
    """Read recipient emails from CSV file."""
    recipients = []
    with open(path, newline='', encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            email = row.get("email")
            if email:
                recipients.append(email.strip())
    return recipients

def read_sent_set(log_path=LOG_FILE):
    """Read log file and return set of recipients already successfully sent."""
    sent = set()
    try:
        with open(log_path, newline='', encoding="utf-8") as f:
            reader = csv.DictReader(f)
            for row in reader:
                if row.get("status","").upper() == "SUCCESS":
                    sent.add(row.get("recipient"))
    except FileNotFoundError:
        pass
    return sent

def append_log(recipient, subject, status, error_msg=""):
    """Append a row to the log CSV file with timestamp."""
    timestamp = datetime.utcnow().isoformat()
    header = ["timestamp","recipient","subject","status","error"]
    write_header = False
    try:
        with open(LOG_FILE, "r", encoding="utf-8") as _:
            pass
    except FileNotFoundError:
        write_header = True

    with open(LOG_FILE, "a", newline='', encoding="utf-8") as f:
        writer = csv.writer(f)
        if write_header:
            writer.writerow(header)
        writer.writerow([timestamp, recipient, subject, status, error_msg])

def build_message(subject, body):
    """Build the email message string."""
    return f"Subject: {subject}\n\n{body}"

# -----------------------------
# Main script

def main():
    cfg = load_config()
    sender_email = cfg["sender_email"]
    password = cfg["password"]
    subject = cfg.get("subject", "Hello")
    body = cfg.get("body", "")

    recipients = read_recipients()
    if not recipients:
        print("No recipients found in", EMAILS_FILE)
        return

    sent_set = read_sent_set()

    # Connect to SMTP server
    server = smtplib.SMTP(cfg.get("smtp_server", "smtp.gmail.com"), cfg.get("smtp_port", 587))
    server.ehlo()
    server.starttls()
    server.ehlo()
    try:
        server.login(sender_email, password)
    except Exception as e:
        print("SMTP login failed:", e)
        return

    for r in recipients:
        if r in sent_set:
            print(f"skip (already sent): {r}")
            continue

        msg = build_message(subject, body)
        success = False
        last_error = ""
        for attempt in range(1, RETRIES+2):
            try:
                server.sendmail(sender_email, r, msg)
                success = True
                append_log(r, subject, "SUCCESS", "")
                print(f"Sent ✅ {r}")
                break
            except Exception as e:
                last_error = str(e)
                print(f"Attempt {attempt} failed for {r}: {e}")
                time.sleep(1)
        if not success:
            append_log(r, subject, "FAILED", last_error)
            print(f"Failed ❌ {r} — logged.")
        time.sleep(DELAY_SECONDS)

    server.quit()
    print("Done.")

if __name__ == "__main__":
    main()
