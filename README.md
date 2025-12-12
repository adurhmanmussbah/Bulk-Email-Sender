# Bulk-Email-Sender

A production-ready Python automation tool used by **Seven Loops Academy for Programming Training**
to send **training proposals** to schools and educational institutions in a professional,
secure, and UTF-8 safe manner.

The tool ensures correct email formatting, attachment delivery, and logging when
reaching multiple schools efficiently.

---

## 🎓 Use Case

This project is designed to help training academies and education providers:

- Send programming training proposals to schools
- Reach multiple institutions efficiently
- Maintain professional email formatting
- Attach academy profiles or training proposals
- Log delivery results for follow-up

---

## 🚀 Features

- Bulk email sending to schools and institutions
- UTF-8 safe (supports smart quotes, Arabic text, emojis 📧📞)
- Gmail SMTP authentication using App Passwords
- Proposal / profile attachment support (PDF)
- Automatic log folder and file creation
- Secure configuration using `.env`
- Clean, extensible Python codebase

---

## 📁 Project Structure

seven-loops-academy-bulk-proposal-sender/
├── bulk_email.py
├── config.env.example
├── emails_list.txt
├── message_template.txt
├── requirements.txt
├── logs/
└── attachments/



---

## 🔐 Configuration

1. Generate a Gmail **App Password**
2. Copy `config.env.example` → `config.env`
3. Fill in your credentials:

SMTP_SERVER=smtp.gmail.com
SMTP_PORT=587
SENDER_EMAIL=academy_email@gmail.com
SENDER_PASSWORD=your_app_password
SENDER_NAME="Seven Loops Academy"



---

## 📄 Proposal Attachment

Place your academy proposal or profile in:
attachments/Seven_Loops_Academy_Training_Proposal.pdf

-------

## ▶️ How to Run

```bash
pip install -r requirements.txt
python bulk_email.py

Logs are automatically created at:
logs/email_log.txt


🛠 Technologies Used

Python
SMTP (Gmail)
MIME (email + attachments)
python-dotenv
Logging

---------

📌 Target Audience

Schools
Educational institutions
Training centers
Academic partnerships

------------
👤 Author

Abdurhman Mussbah
Founder – Seven Loops Academy
Abu Dhabi, UAE

