from faker import Faker
import random
import string
from pystyle import Add, Center, Anime, Colors, Colorate, Write, System
from os.path import isfile
import requests
import base64, json,os
from datetime import date
from datetime import datetime
from time import sleep,strftime
import requests
import socket
luc = "\033[1;32m"
trang = "\033[1;37m"
do = "\033[1;31m"
vang = "\033[0;93m"
hong = "\033[1;35m"
xduong = "\033[1;34m"
lam = "\033[1;36m"
red='\u001b[31;1m'
yellow='\u001b[33;1m'
green='\u001b[32;1m'
blue='\u001b[34;1m'
tim='\033[1;35m'
xanhlam='\033[1;36m'
xam='\033[1;30m'
black='\033[1;19m'
def generate_email(domain, num_emails, filename, country):
    if country.lower() == 'us':
        fake = Faker('en_US')
    elif country.lower() == 'india':
        fake = Faker('hi_IN')
    elif country.lower() == 'vn':
        fake = Faker('vi_VN')
    elif country.lower() == 'canada':
        fake = Faker('en_CA')
    elif country.lower() == 'singapore':
        fake = Faker('en_SG')
    elif country.lower() == 'sez':
        fake = Faker('fr_FR')
    else:
        print("\033[1;37m" + "Quốc gia không được hỗ trợ. Vui lòng chọn 'US', 'India', 'VN', 'Canada', 'Singapore' hoặc 'Sez'." + "\033[1;33m")
        return

    # Danh sách tên Việt Nam
    vietnamese_names = "Nguyen,Tran,Le,Pham,Ho,Huynh,Hoang,Phan,Vu,Vo,Dang,Bui,Do,Hua,Ly,Cao,Dinh,Doan,Dao,Duc,Duong,Giang,Ha,Han,Khuat,Khuong,La,Lam,Luc,Mai,Mac,Nghe,Nghiem,Ngo,Ngo,Nguyen,Pho,Quach,Quang,Quan,Quy,Ta,Thai,Thach,Than,Thang,Thao,Thi,Thich,Thinh,Thoi,Tieu,To,Trang,Trinh,Trinh,Truong,Tu,Ung,Vien,Vuong,Vuu,Yen,Van,Thi,Dinh..."

    # Chuyển đổi danh sách tên thành một danh sách
    vietnamese_names = vietnamese_names.split(',')

    # Hỏi người dùng có muốn thêm số vào tên không
    use_numbers = input("\033[1;37m" + "\033[1;97m[\033[1;91m❣\033[1;97m] \033[1;36m✈  \033[1;32mBạn có muốn thêm số vào tên không? (y/n): " + "\033[1;33m")
    use_numbers = True if use_numbers.lower() == 'y' else False

    # Hỏi người dùng muốn thêm ký tự gì vào tên
    char_to_add = input("\033[1;37m" + "\033[1;97m[\033[1;91m❣\033[1;97m] \033[1;36m✈  \033[1;32mBạn muốn thêm ký tự gì vào sau tên? (\033[1;97m[\033[1;91m❣\033[1;97m] \033[1;36m✈  \033[1;32mNhập 'không' nếu bạn không muốn thêm ký tự): " + "\033[1;33m")

    with open(filename, 'w') as f:
        for _ in range(num_emails):
            if country.lower() == 'vn':
                # Chọn một tên ngẫu nhiên từ danh sách tên Việt Nam
                name = random.choice(vietnamese_names).lower()
            else:
                # Chọn một tên ngẫu nhiên từ danh sách tên Mỹ/Canada/Ấn Độ/Singapore/Sez
                name = fake.first_name().lower()

            # Thêm số vào tên nếu người dùng chọn
            if use_numbers:
                name += str(random.randint(0, 99))

            # Thêm ký tự vào tên nếu người dùng chọn
            if char_to_add.lower() != 'không':
                name += char_to_add

            email = name + '@' + domain
            print("\033[1;36m" + "HuongDev | " + email + " |" + "\033[0m")
            f.write(email + '\n')
import os,sys
import pywifi
from requests import session
from colorama import Fore, Style
import requests, random, re
from random import randint
import requests,pystyle
from pystyle import Add, Center, Anime, Colors, Colorate, Write, System
from datetime import date
from datetime import datetime
time=datetime.now().strftime("%H:%M:%S")
from pystyle import *
data_machine = []
today = date.today()
now = datetime.now()
thu = now.strftime("%A")
ngay_hom_nay = now.strftime("%d")
thang_nay = now.strftime("%m")
nam_ = now.strftime("%Y")
def check_internet_connection():
    try:
        response = requests.get("http://www.google.com", timeout=5)
        return True
    except requests.ConnectionError:
        return False

# Kiểm tra kết nối internet
if check_internet_connection():
    print(f"{luc}Vui Lòng Chờ!!!")
    sleep(0.1)
else:
    print(f"{do}Vui Lòng Kiểm Tra Kết NốI!!!")
    sys.exit()
def get_location_by_ip():
    try:
        response = requests.get("https://ipinfo.io")
        data = response.json()

        city = data.get("city")
        region = data.get("region")
        country = data.get("country")
        loc = data.get("loc").split(",")
        latitude, longitude = loc if len(loc) == 2 else (None, None)

        return city, region, country, latitude, longitude
    except Exception as e:
        print(f"Lỗi: {e}")
        return None, None, None, None, None
city, region, country, latitude, longitude = get_location_by_ip()
def get_weather():
    try:
        # Lấy thông tin vị trí từ dịch vụ ipinfo.io
        response = requests.get("https://ipinfo.io")
        data = response.json()
        location = data.get("loc").split(",")
        latitude, longitude = location
        # Lấy thông tin thời tiết từ trang web công cộng
        base_url = f"https://wttr.in/{latitude},{longitude}?format=%t"
        response = requests.get(base_url)
        weather_description = response.text.strip()
        return weather_description
    except Exception as e:
        print(f"Lỗi: {e}")
        return None
weather_description = get_weather()
System.Clear()
if __name__ == "__main__":
    print(f"""
\033[1;33m██      ██╗      ████████╗ █████╗  █████╗ ██╗
\033[1;35m██╗    ╔██║      ╚══██╔══╝██╔══██╗██╔══██╗██║
\033[1;36m██║████║██║ █████╗  ██║   ██║  ██║██║  ██║██║
\033[1;37m██║    ╚██║ ╚════╝  ██║   ██║  ██║██║  ██║██║
\033[1;32m██║     ██║         ██║   ╚█████╔╝╚█████╔╝██████╗
\033[1;31m╚═╝     ╚═╝         ╚═╝    ╚════╝  ╚════╝ ╚═════╝\n
\033[1;97mTool By: \033[1;32mTrịnh Hướng            \033[1;97mPhiên Bản: \033[1;32m4.0     
\033[97m════════════════════════════════════════════════  
\033[1;97m[\033[1;91m❣\033[1;97m]\033[1;97m Tool   \033[1;31m  : \033[1;97m☞ \033[1;31mGen Mail V2♔ \033[1;97m☜
\033[1;97m[\033[1;91m❣\033[1;97m]\033[1;97m Tik Tok\033[1;31m  : \033[1;33mhttps:\033[1;32m//www.tiktok.com\033[1;31m/m@huongdev27
\033[1;97m[\033[1;91m❣\033[1;97m]\033[1;97m Zalo\033[1;31m     : \033[1;97m☞\033[1;31m0\033[1;37m3\033[1;36m6\033[1;35m2\033[1;34m1\033[1;33m6\033[1;33m6\033[1;34m8\033[1;35m6\033[1;37m3☜
\033[1;97m[\033[1;91m❣\033[1;97m]\033[1;97m Facebook\033[1;31m : \033[1;97mi.urs.bin.python.TrinhHuong 
\033[1;97m[\033[1;91m❣\033[1;97m]\033[1;97m Telegram\033[1;31m : \033[1;97m☞\033[1;32mhttps://t.me/+77MuosyD-yk4MGY1🔫\033[1;97m☜
\033[97m════════════════════════════════════════════════
\033[1;97m[\033[1;91m❣\033[1;97m]\033[1;97m Youtube\033[1;31m  : \033[1;97m☞ \033[1;36mHướng Dev - Kiếm Tiền Online\033[1;31m♔ \033[1;97m☜""")
    domain = input("\033[1;37m" + "\033[1;97m[\033[1;91m❣\033[1;97m] \033[1;36m✈  \033[1;32mNhập tên miền của email (ví dụ: yahoo.com): " + "\033[1;33m")
    num_emails = int(input("\033[1;37m" + "\033[1;97m[\033[1;91m❣\033[1;97m] \033[1;36m✈  \033[1;32mNhập số lượng email bạn muốn tạo: " + "\033[1;33m"))
    filename = input("\033[1;37m" + "\033[1;97m[\033[1;91m❣\033[1;97m] \033[1;36m✈  \033[1;32mNhập tên file txt để lưu email: " + "\033[1;33m")
    country = input("\033[1;37m" + "\033[1;97m[\033[1;91m❣\033[1;97m] \033[1;36m✈  \033[1;32mChọn quốc gia để tạo tên (US, India, VN, Canada, Singapore, Sez): " + "\033[1;33m")
    generate_email(domain, num_emails, filename, country)