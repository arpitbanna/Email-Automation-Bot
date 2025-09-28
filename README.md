# 📧 Email Automation Bot

A professional Python bot for sending automated emails to a list of recipients using SMTP.  
This project demonstrates a practical automation system with logging, error handling, and resumable sending, making it ideal for testing, newsletters, or personal projects.

---

## 🛠 Features
- Reads recipient emails from a CSV file (`emails.csv`)  
- Uses `config.json` for configuration: sender email, app password, subject, and body  
- Sends emails automatically to multiple recipients  
- Logs each email's success or failure to `sent_log.csv`  
- Prevents duplicate sending by checking previous logs  
- Easy to customize, extend, and integrate with other systems  

---

## 📂 Project Structure
```
SendEmail/
│── send_email.py       # Main Python script
│── config.json         # Configuration file for email settings
│── emails.csv          # List of recipient emails
│── sent_log.csv        # Logs of sent emails (automatically created)
│── README.md           # Project documentation
```

---

## ⚡ Requirements
- Python 3.x  
- Internet connection for sending emails  
- Optional: `pandas` if you prefer CSV processing with pandas  

---

## 🚀 Usage
1. Add recipient emails in `emails.csv` with a header `email`:
```csv
email
alice@example.com
bob@example.com
```
2. Update `config.json` with your sender email, app password, subject, and body:
```json
{
  "sender_email": "your_email@gmail.com",
  "password": "your_app_password",
  "subject": "Hello from SllHex",
  "body": "This is an automated message sent via Python bot.",
  "smtp_server": "smtp.gmail.com",
  "smtp_port": 587
}
```
3. Run the script:
```bash
python send_email.py
```
4. Check `sent_log.csv` to see which emails were sent successfully and which failed.

---

## 🔒 Important Notes
- For Gmail accounts, enable **2FA** and use an **App Password**.  
- Do **not** use your main email password for security reasons.  
- Avoid sending too many emails too quickly to prevent being blocked by your email provider.  
- The log system ensures that emails are not resent to the same recipient.

---

## 🔧 Future Improvements
- Add advanced logging and reporting features  
- Support command-line arguments for dynamic input  
- Dockerize the project for easier deployment  
- Integrate AI-generated email content for personalized messages  
- Add retry mechanisms with exponential backoff for failed emails  

---

## 🎯 Purpose & Benefits
This project is a practical demonstration of:
- Real-world Python automation  
- Working with CSV and JSON files  
- Email protocols (SMTP) and security best practices  
- Error handling and logging systems  

It is a strong showcase for potential employers or clients to see your **hands-on programming and automation skills**.
