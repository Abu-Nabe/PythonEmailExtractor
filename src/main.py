import re
import requests
from bs4 import BeautifulSoup

from utils import get_email_urls

# Get list of URLs from .env
email_urls = get_email_urls()

def extract_emails_from_url(url):
    """Fetch emails from a given URL using regex."""
    try:
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
        }
        response = requests.get(url, headers=headers)
        response.raise_for_status()

        soup = BeautifulSoup(response.text, "html.parser")
        text = soup.get_text()

        # Regex to find emails
        email_pattern = r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"
        emails = set(re.findall(email_pattern, text))

        return emails
    except Exception as e:
        print(f"❌ Error fetching {url}: {e}")
        return set()

# Extract emails from each URL in the list
all_emails = {}

for url in email_urls:
    extracted = extract_emails_from_url(url)
    all_emails[url] = list(extracted)  # Convert set to list

# Print Results
for url, emails in all_emails.items():
    print(f"\n🔗 URL: {url}")
    if emails:
        print("📩 Extracted Emails:", emails)
    else:
        print("⚠️ No emails found.")
