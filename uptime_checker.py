import requests
from dotenv import load_dotenv
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import os

# Load konfigurasi dari .env
load_dotenv()

# Daftar website yang akan dipantau
websites = ["https://www.google.com", "https://anu123.com"]

# Konfigurasi email
EMAIL_ADDRESS = os.getenv("EMAIL_ADDRESS")  # Masukkan email pengirim di .env
EMAIL_PASSWORD = os.getenv("EMAIL_PASSWORD")  # Masukkan password di .env
EMAIL_RECIPIENT = os.getenv("EMAIL_RECIPIENT")  # Masukkan email penerima di .env
SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587

# Fungsi untuk mengirim email
def send_email(subject, body):
    try:
        msg = MIMEMultipart()
        msg['From'] = EMAIL_ADDRESS
        msg['To'] = EMAIL_RECIPIENT
        msg['Subject'] = subject

        msg.attach(MIMEText(body, 'plain'))
        server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
        server.starttls()
        server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
        server.send_message(msg)
        server.quit()

        print(f"Email sent: {subject}")
    except Exception as e:
        print(f"Failed to send email: {e}")

# Fungsi untuk memeriksa status website
def check_website():
    messages = []  # Simpan pesan status website
    for website in websites:
        try:
            response = requests.get(website, timeout=5)
            if response.status_code == 200:
                print(f"{website} is UP.")
                messages.append(f"{website} is UP.")
            else:
                print(f"{website} is DOWN. Status code: {response.status_code}")
                messages.append(f"{website} is DOWN. Status code: {response.status_code}")
        except requests.exceptions.RequestException as e:
            print(f"{website} is DOWN. Error: {e}")
            messages.append(f"{website} is DOWN. Error: {e}")

    # Gabungkan semua pesan dan kirim email
    if messages:
        email_body = "\n".join(messages)
        send_email("Website Uptime Status", email_body)

# Jalankan pengecekan satu kali
print("Website Uptime Checker is running...")
check_website()
print("Website Uptime Checker has finished.")
