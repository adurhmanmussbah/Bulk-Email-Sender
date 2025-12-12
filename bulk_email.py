import os
import smtplib
import logging
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
from email.header import Header
from dotenv import load_dotenv

# -----------------------------------------
# Load Config
# -----------------------------------------
load_dotenv("config.env")

SMTP_SERVER = os.getenv("SMTP_SERVER")
SMTP_PORT = int(os.getenv("SMTP_PORT"))
SENDER_EMAIL = os.getenv("SENDER_EMAIL")
SENDER_PASSWORD = os.getenv("SENDER_PASSWORD")
SENDER_NAME = os.getenv("SENDER_NAME")

# -----------------------------------------
# Dynamic Logging Setup
# -----------------------------------------
LOG_DIR = "logs"
LOG_FILE = "email_log.txt"

if not os.path.exists(LOG_DIR):
    os.makedirs(LOG_DIR)

LOG_PATH = os.path.join(LOG_DIR, LOG_FILE)

logging.basicConfig(
    filename=LOG_PATH,
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

# -----------------------------------------
# Send Email Function
# -----------------------------------------
def send_email(recipient, subject, message_body, attachment_path=None):
    try:
        msg = MIMEMultipart()
        msg["From"] = str(Header(f"{SENDER_NAME} <{SENDER_EMAIL}>", "utf-8"))
        msg["To"] = recipient
        msg["Subject"] = Header(subject, "utf-8")

        msg.attach(MIMEText(message_body, "plain", "utf-8"))

        # Attach Proposal
        if attachment_path:
            with open(attachment_path, "rb") as f:
                file_part = MIMEApplication(
                    f.read(),
                    Name=os.path.basename(attachment_path)
                )
            file_part["Content-Disposition"] = (
                f'attachment; filename="{os.path.basename(attachment_path)}"'
            )
            msg.attach(file_part)

        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.ehlo()
            server.starttls()
            server.ehlo()
            server.login(SENDER_EMAIL, SENDER_PASSWORD)
            server.sendmail(
                SENDER_EMAIL,
                recipient,
                msg.as_string().encode("utf-8")
            )

        logging.info(f"SUCCESS - Email sent to {recipient}")
        print(f"[OK] Email sent to {recipient}")

    except Exception as e:
        logging.error(f"FAILED - {recipient} - {e}")
        print(f"[ERROR] Could not send email to {recipient} - {e}")

# -----------------------------------------
# Main Execution
# -----------------------------------------
def main():
    with open("emails_list.txt", "r", encoding="utf-8") as f:
        recipients = [line.strip() for line in f if line.strip()]

    with open("message_template.txt", "r", encoding="utf-8") as f:
        message = f.read()

    # ✅ EMAIL SUBJECT
    subject = "Programming Training Proposal – Seven Loops Academy"

    for email in recipients:
        send_email(
            recipient=email,
            subject=subject,
            message_body=message,
            # ✅ ATTACHMENT PATH
            attachment_path="attachments/Seven_Loops_Academy_Training_Proposal.pdf"
        )

if __name__ == "__main__":
    main()
