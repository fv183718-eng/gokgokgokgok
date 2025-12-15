import socket
import requests

# ===== INPUT URL =====
url = input("Masukkan URL (contoh: https//gokgok.com): ")

# ===== BERSIHKAN URL =====
domain = url.replace("https://", "").replace("http://", "").split("/")[0]

print("\nDomain :", domain)

try:
    # ===== KONVERSI DOMAIN KE IP =====
    ip = socket.gethostbyname(domain)
    print("IP Address :", ip)

    # ===== LACAK INFO IP =====
    api_url = f"http://ip-api.com/json/{ip}"
    data = requests.get(api_url).json()

    print("\nHASIL PELACAKAN IP")
    if data["status"] == "success":
        print("Negara     :", data["country"])
        print("Provinsi   :", data["regionName"])
        print("Kota       :", data["city"])
        print("ISP        :", data["isp"])
        print("Latitude   :", data["lat"])
        print("Longitude  :", data["lon"])
    else:
        print("Gagal melacak IP")

except socket.gaierror:
    print("URL tidak valid atau tidak dapat diakses")
