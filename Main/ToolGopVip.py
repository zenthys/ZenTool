import threading, base64, os, time, re, json, random
from datetime import datetime, timedelta
from time import sleep, strftime
from bs4 import BeautifulSoup
import requests, socket, sys
from cryptography.fernet import Fernet
from concurrent.futures import ThreadPoolExecutor
try:
  from faker import Faker
  from requests import session
  from colorama import Fore, Style
  import requests, random, re
  from random import randint
  import requests,pystyle
  import socks
except:
  os.system("pip install faker")
  os.system("pip install requests")
  os.system("pip install colorama")
  os.system('pip install requests && pip install bs4 && pip install pystyle')
  os.system("pip3 install requests pysocks")
  print('__Vui Lòng Chạy Lại Tool__')
try:
    with open("secret.key", "rb") as key_file:
        secret_key = key_file.read()
except FileNotFoundError:
    secret_key = Fernet.generate_key()
    with open("secret.key", "wb") as key_file:
        key_file.write(secret_key)

cipher = Fernet(secret_key)
from pystyle import Add, Center, Anime, Colors, Colorate, Write, System
xnhac = "\033[1;36m"
do = "\033[1;31m"
luc = "\033[1;32m"
vang = "\033[1;33m"
xduong = "\033[1;34m"
hong = "\033[1;35m"
trang = "\033[1;39m"
whiteb="\033[1;39m"
red="\033[0;31m"
redb="\033[1;31m"
end='\033[0m'
dev="\033[1;39m[\033[1;31m×\033[1;39m]\033[1;39m"

def banner():
 banner = f"""
\033[1;33m██      ██╗      ████████╗ █████╗  █████╗ ██╗
\033[1;35m██╗    ╔██║      ╚══██╔══╝██╔══██╗██╔══██╗██║
\033[1;36m██║████║██║ █████╗  ██║   ██║  ██║██║  ██║██║
\033[1;37m██║    ╚██║ ╚════╝  ██║   ██║  ██║██║  ██║██║
\033[1;32m██║     ██║         ██║   ╚█████╔╝╚█████╔╝██████╗
\033[1;31m╚═╝     ╚═╝         ╚═╝    ╚════╝  ╚════╝ ╚═════╝\n
\033[1;97mTool By: \033[1;32mTrịnh Hướng            \033[1;97mPhiên Bản: \033[1;32m4.0     
\033[97m════════════════════════════════════════════════  
\033[1;97m[\033[1;91m❣\033[1;97m]\033[1;97m Youtube\033[1;31m  : \033[1;97m☞ \033[1;36mHướng Dev - Kiếm Tiền Online\033[1;31m♔ \033[1;97m☜
\033[1;97m[\033[1;91m❣\033[1;97m]\033[1;97m Tik Tok\033[1;31m  : \033[1;33mhttps:\033[1;32m//www.tiktok.com\033[1;31m/m@huongdev27
\033[1;97m[\033[1;91m❣\033[1;97m]\033[1;97m Zalo\033[1;31m     : \033[1;97m☞\033[1;31m0\033[1;37m3\033[1;36m6\033[1;35m2\033[1;34m1\033[1;33m6\033[1;33m6\033[1;34m8\033[1;35m6\033[1;37m3☜
\033[1;97m[\033[1;91m❣\033[1;97m]\033[1;97m Facebook\033[1;31m : \033[1;97mi.urs.bin.python.TrinhHuong 
\033[1;97m[\033[1;91m❣\033[1;97m]\033[1;97m Telegram\033[1;31m : \033[1;97m☞\033[1;32mhttps://t.me/+77MuosyD-yk4MGY1🔫\033[1;97m☜
\033[97m════════════════════════════════════════════════
"""
 for X in banner:
  sys.stdout.write(X)
  sys.stdout.flush() 
  sleep(0.000001)
def bes4(url):
    # Gửi yêu cầu GET đến URL
    response = requests.get(url)
    
    # Nếu yêu cầu thành công (status code 200)
    if response.status_code == 200:
        # Phân tích nội dung HTML của trang web
        soup = BeautifulSoup(response.content, 'html.parser')
        
        # Tìm thẻ <span> chứa thông tin phiên bản và trạng thái bảo trì
        version_tag = soup.find('span', id='version0')
        maintenance_tag = soup.find('span', id='maintenance0')
        
        # Lấy nội dung văn bản bên trong thẻ
        version = version_tag.text.strip() if version_tag else None
        maintenance = maintenance_tag.text.strip() if maintenance_tag else None
        
        return version, maintenance
    
    return None, None

def checkver():
    url = 'https://checkserver.hotrommo.com/'
    version, maintenance = bes4(url)
    
    if maintenance == 'on':
        print("Tool đang được bảo trì. Vui lòng thử lại sau. \nHoặc vào nhóm Tele: https://t.me/+77MuosyD-yk4MGY1")
        sys.exit()
    
    return version

# Sử dụng hàm checkver để kiểm tra phiên bản
current_version = checkver()
if current_version:
  
    print(f"Phiên bản hiện tại: {current_version}")
else:
    print("Không thể lấy thông tin phiên bản hoặc tool đang được bảo trì.")
# Hàm để lấy địa chỉ IP của thiết bị

def get_ip_address():
    try:
        hostname = socket.gethostname()
        ip_address = socket.gethostbyname(hostname)
        return ip_address
    except:
        return None

# Hàm để hiển thị địa chỉ IP của thiết bị
def display_ip_address(ip_address):
    if ip_address:
        banner = """
\033[1;33m██      ██╗      ████████╗ █████╗  █████╗ ██╗
\033[1;35m██╗    ╔██║      ╚══██╔══╝██╔══██╗██╔══██╗██║
\033[1;36m██║████║██║ █████╗  ██║   ██║  ██║██║  ██║██║
\033[1;37m██║    ╚██║ ╚════╝  ██║   ██║  ██║██║  ██║██║
\033[1;32m██║     ██║         ██║   ╚█████╔╝╚█████╔╝██████╗
\033[1;31m╚═╝     ╚═╝         ╚═╝    ╚════╝  ╚════╝ ╚═════╝\n
\033[1;97mTool By: \033[1;32mTrịnh Hướng            \033[1;97mPhiên Bản: \033[1;32m4.0     
\033[97m════════════════════════════════════════════════  
\033[1;97m[\033[1;91m❣\033[1;97m]\033[1;97m Tool   \033[1;31m  : \033[1;97m☞ \033[1;31mTool Gộp Vip♔ \033[1;97m☜
\033[1;97m[\033[1;91m❣\033[1;97m]\033[1;97m Tik Tok\033[1;31m  : \033[1;33mhttps:\033[1;32m//www.tiktok.com\033[1;31m/m@huongdev27
\033[1;97m[\033[1;91m❣\033[1;97m]\033[1;97m Zalo\033[1;31m     : \033[1;97m☞\033[1;31m0\033[1;37m3\033[1;36m6\033[1;35m2\033[1;34m1\033[1;33m6\033[1;33m6\033[1;34m8\033[1;35m6\033[1;37m3☜
\033[1;97m[\033[1;91m❣\033[1;97m]\033[1;97m Facebook\033[1;31m : \033[1;97mi.urs.bin.python.TrinhHuong 
\033[1;97m[\033[1;91m❣\033[1;97m]\033[1;97m Telegram\033[1;31m : \033[1;97m☞\033[1;32mhttps://t.me/+77MuosyD-yk4MGY1🔫\033[1;97m☜
\033[97m════════════════════════════════════════════════
\033[1;97m[\033[1;91m❣\033[1;97m]\033[1;97m Youtube\033[1;31m  : \033[1;97m☞ \033[1;36mHướng Dev - Kiếm Tiền Online\033[1;31m♔ \033[1;97m☜
"""

        os.system('cls' if os.name == 'nt' else 'clear')
        for x in banner:
            print(x, end="")
            time.sleep(0.001)

        print(f"\033[1;32mĐịa chỉ IP : {ip_address}     Version: {current_version}")
    else:
        print("Không thể lấy địa chỉ IP của thiết bị.")

# Hàm để lưu thông tin IP và key vào tệp tin JSON
def luu_thong_tin_ip(ip, key, expiration_date):
    data = {ip: {'key': key, 'expiration_date': expiration_date.isoformat()}}
    json_data = json.dumps(data).encode()
    encrypted_data = cipher.encrypt(json_data)

    with open('ip_key.json', 'wb') as file:
        file.write(encrypted_data)

# Hàm tải thông tin từ tệp tin JSON đã mã hóa
def tai_thong_tin_ip():
    try:
        with open('ip_key.json', 'rb') as file:
            encrypted_data = file.read()
        decrypted_data = cipher.decrypt(encrypted_data)
        data = json.loads(decrypted_data)
        return data
    except FileNotFoundError:
        return None
# Hàm để kiểm tra xem IP đã sử dụng key chưa và key còn hạn hay không
def kiem_tra_ip(ip):
    try:
        with open('ip_key.json', 'rb') as file:
            encrypted_data = file.read()

        # Giải mã dữ liệu
        decrypted_data = cipher.decrypt(encrypted_data)
        data = json.loads(decrypted_data)

        if ip in data:
            expiration_date = datetime.fromisoformat(data[ip]['expiration_date'])
            if expiration_date > datetime.now():
                return data[ip]['key']
        return None
    except (FileNotFoundError, KeyError, TypeError, ValueError) as e:
        # print(f"Lỗi khi kiểm tra key: {e}")
        return None


# Hàm để tạo key và URL mới dựa trên IP hiện tại
def generate_key_and_url(ip_address):
    ngay = int(datetime.now().day)
    key1 = str(ngay * 27 + 27)
    
    # Xử lý địa chỉ IP để chỉ lấy các số
    ip_numbers = ''.join(filter(str.isdigit, ip_address))
        
    key = f'huongdev{key1}{ip_numbers}'
    # Thời gian hết hạn là 23:59:00 hôm nay
    expiration_date = datetime.now().replace(hour=23, minute=59, second=0, microsecond=0)
    url = f'https://huongdev.com/?key={key}'
    return url, key, expiration_date

# Hàm để kiểm tra xem đã qua 00:00:01 của ngày mới chưa
def da_qua_gio_moi():
    now = datetime.now()
    midnight = now.replace(hour=0, minute=0, second=0, microsecond=0) + timedelta(days=1)
    start_new_day = midnight + timedelta(seconds=1)
    return now >= start_new_day
# Chương trình chính
def main():
    # Lấy và hiển thị địa chỉ IP của thiết bị
    ip_address = get_ip_address()
    display_ip_address(ip_address)

    # Kiểm tra và tạo link rút gọn để vượt key cho từng địa chỉ IP
    if ip_address:
        existing_key = kiem_tra_ip(ip_address)
        if existing_key:
            print(f"\033[1;35mTool còn hạn, mời bạn dùng tool. ")
            sleep(2)
        else:
            url, key, expiration_date = generate_key_and_url(ip_address)
            print(url)
            # token_yeumoney = 'f7e85811bc83948a0a66e121fa312afc03472eabd86a53c4bc9ec86662a480c8'
            # yeumoney_response = requests.get(f'https://yeumoney.com/QL_api.php?token={token_yeumoney}&format=json&url={url}')
            yeumoney_response = requests.get(f'https://dilink.net/JSON_QL_API.php?token=7547feb041956891c2e2c2d5ca29080039c12b4ed7fa4c4273a85ba17bb5bc87&url=url={url}')
            # print(yeumoney_response)
            if yeumoney_response.status_code == 200:
                yeumoney_data = yeumoney_response.json()
                print(yeumoney_data)
                if yeumoney_data.get('status') == "error":
                    print(yeumoney_data.get('message'))
                    quit()
                else:
                    link_key = yeumoney_data.get('shortenedUrl')
                    print(link_key)
                    token_link4m = '66358d4299686f733016d95a'
                    link4m_response = requests.get(f'https://link4m.co/api-shorten/v2?api={token_link4m}&format=json&url={link_key}')
                    print("\033[1;31mLưu Ý: \033[1;33mTool Free Nhé Cả Nhà Yêu \033[1;91m❣\033[1;32m")
                    # Kiểm tra kết quả trả về từ link rút gọn
                    if link4m_response.status_code == 200:
                        link4m_data = link4m_response.json()
                        if link4m_data.get('status') == "error":
                            print(link4m_data.get('message'))
                            quit()
                        else:
                            link_key = link4m_data.get('shortenedUrl')
                            print('Link Để Vượt Key Là:', link_key)  # Sử dụng dấu phẩy thay vì dấu cộng
                    else:
                        print('Không thể kết nối đến dịch vụ rút gọn URL')
                        quit()
            else:
                print('Không thể kết nối đến dịch vụ rút gọn URL')
                quit()

            # Yêu cầu người dùng nhập key
            while True:
                keynhap = input('Key Đã Vượt Là: ')

                # Kiểm tra key nhập vào với key được tạo ra từ IP hiện tại
                if keynhap == key:
                    print('Key Đúng Mời Bạn Dùng Tool')
                    sleep(2)
                    luu_thong_tin_ip(ip_address, keynhap, expiration_date)
                    break
                else:
                    print('Key Sai Vui Lòng Vượt Lại Link:', link_key)
        
        # Kiểm tra nếu đã qua 00:00:01 của ngày mới
        if da_qua_gio_moi():
            print("Key của bạn đã hết hạn. Đợi 2 giây để lấy key mới từ ngày mới...")
            time.sleep(2)
            main()  # Gọi lại main() để lấy key mới từ ngày mới
if __name__ == "__main__":
    main()
while True:
    exec(requests.get('https://raw.githubusercontent.com/trinhhuong2004/ToolGop/main/index.py').text)
