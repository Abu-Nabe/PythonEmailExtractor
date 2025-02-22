import os
from dotenv import load_dotenv

# Load environment variables from .env file once
load_dotenv()

def get_emails_urls():
    """Retrieve emails from .env and return as a list."""
    emails = os.getenv("EMAIL_URLS", "").split(",")
    return [email.strip() for email in emails if email.strip()]
