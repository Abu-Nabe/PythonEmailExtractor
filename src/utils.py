import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

def get_email_urls():
    """Retrieve URLs from .env and return them as a list."""
    urls = os.getenv("EMAIL_URLS", "").split(",")
    return [url.strip() for url in urls if url.strip()]
