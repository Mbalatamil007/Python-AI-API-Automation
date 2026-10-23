import os
import smtplib

from email.message import EmailMessage
from dotenv import load_dotenv


load_dotenv()


def send_email(question, ai_response):

    sender = os.getenv("GMAIL_SENDER")
    password = os.getenv("GMAIL_APP_PASSWORD")
    receiver = os.getenv("GMAIL_RECEIVER")

    if not all([sender, password, receiver]):
        raise ValueError(
            "Gmail configuration is missing in .env"
        )

    # Create email
    message = EmailMessage()

    message["From"] = sender
    message["To"] = receiver
    message["Subject"] = "AI API Automation - Generated Response"

    email_body = f"""
Hello,

Your AI-generated response is ready.

Question:
{question}

AI Response:
{ai_response}

Regards,
Python AI API Automation
"""

    message.set_content(email_body)

    # Send email using Gmail SMTP
    with smtplib.SMTP_SSL(
        "smtp.gmail.com",
        465,
        timeout=30
    ) as server:

        server.login(sender, password)

        server.send_message(message)

    return True