import requests
from dotenv import load_dotenv
import os
import yagmail

# Load konfigurasi dari .env
load_dotenv()
EMAIL = os.getenv("EMAIL")
EMAIL_PASSWORD = os.getenv("EMAIL_PASSWORD")
ALERT_RECIPIENT = os.getenv("ALERT_RECIPIENT")

websites = ["https://www.google.com", "https://anu123.com"]

def send_email(subject, body):
    try:
        yag = yagmail.SMTP(EMAIL, EMAIL_PASSWORD)
        yag.send(to=ALERT_RECIPIENT, subject=subject, contents=body)
        print(f"Email sent to {ALERT_RECIPIENT}")
    except Exception as e:
        print(f"Failed to send email: {e}")

def check_website():
    for website in websites:
        try:
            response = requests.get(website, timeout=5)
            if response.status_code == 200:
                print(f"{website} is UP.")
            else:
                print(f"{website} is DOWN. Status code: {response.status_code}")
                send_email(
                    subject=f"Website Down: {website}",
                    body=f"{website} is down. Status code: {response.status_code}"
                )
        except requests.exceptions.RequestException as e:
            print(f"{website} is DOWN. Error: {e}")
            send_email(
                subject=f"Website Down: {website}",
                body=f"{website} is down. Error: {e}"
            )

print("Website Uptime Checker is running...")
check_website()
print("Website Uptime Checker has finished.")
