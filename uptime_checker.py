import requests
import schedule
import time
from dotenv import load_dotenv
import os

# Load konfigurasi dari .env
load_dotenv()


# Daftar website yang akan dipantau
websites = ["https://www.google.com", "https://anu123.com"]


# Fungsi untuk memeriksa status website
def check_website():
    for website in websites:
        try:
            response = requests.get(website, timeout=5)
            if response.status_code == 200:
                print(f"{website} is UP.")
            else:
                print(f"{website} is DOWN. Status code: {response.status_code}")
                
        except requests.exceptions.RequestException as e:
            print(f"{website} is DOWN. Error: {e}")
           

# Jadwalkan pengecekan setiap 5 menit
schedule.every(1).minutes.do(check_website)

print("Website Uptime Checker is running...")
while True:
    schedule.run_pending()
    time.sleep(1)