# Gunakan image Python sebagai base image
FROM python:3.8-slim

# Set working directory
WORKDIR /app

# Salin file requirements.txt ke dalam container
COPY requirements.txt /app/

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Salin seluruh aplikasi ke dalam container
COPY . /app

# Tentukan port yang digunakan oleh aplikasi
EXPOSE 5000

# Perintah untuk menjalankan aplikasi
CMD ["python", "uptime_checker.py"]
