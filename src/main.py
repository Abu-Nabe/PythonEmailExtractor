import re
import requests
from bs4 import BeautifulSoup

def extract_emails_from_url(url):
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
        print(f"Error fetching {url}: {e}")
        return set()

# Example Usage
url = "https://www.iana.org/domains/reserved"
emails = extract_emails_from_url(url)

if emails:
    print("Extracted Emails:", emails)
else:
    print("No emails found.")
