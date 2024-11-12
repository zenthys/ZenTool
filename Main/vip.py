#cre : HuongDev
#zalo : 0362166863
import threading,base64
import os,time,re,json,random
from datetime import datetime, timedelta
from time import sleep,strftime
from bs4 import BeautifulSoup
import requests
import os, sys
import socket

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
    try:
        # Gửi yêu cầu GET đến URL
        response = requests.get(url)
        response.raise_for_status()  # Kiểm tra nếu có lỗi HTTP

        # Phân tích nội dung HTML của trang web
        soup = BeautifulSoup(response.content, 'html.parser')

        # Tìm thẻ <span> chứa thông tin phiên bản, trạng thái bảo trì và ngày hết hạn
        version_tag = soup.find('span', id='version0')
        maintenance_tag = soup.find('span', id='maintenance0')
        end_date_tag = soup.find('span', id='endate0')

        # Lấy nội dung văn bản bên trong thẻ
        version = version_tag.text.strip() if version_tag else None
        maintenance = maintenance_tag.text.strip() if maintenance_tag else None
        endate = end_date_tag.text.strip() if end_date_tag else None

        return version, maintenance, endate

    except requests.RequestException as e:
        print(f"Lỗi khi truy cập URL: {e}")
        return None, None, None

def checkver():
    url = 'https://huongdz.hotrommo.com/'  # URL mẫu của bạn
    version, maintenance, endate = bes4(url)

    if maintenance == 'on':
        print("Tool đang được bảo trì. Vui lòng thử lại sau. \nHoặc vào nhóm Tele: https://t.me/+77MuosyD-yk4MGY1")
        sys.exit()

    return version, endate

# Sử dụng hàm checkver để kiểm tra phiên bản và ngày hết hạn
current_version, current_endate = checkver()

if current_version:
    print(f"Phiên bản hiện tại: {current_version}")
else:
    print("Không thể lấy thông tin phiên bản.")

if current_endate:
    print(f"Ngày hết hạn tool: {current_endate}")
else:
    print("Không thể lấy ngày hết hạn tool.")
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
    else:
        print("Không thể lấy địa chỉ IP của thiết bị.")

# Hàm để lưu thông tin IP và key vào tệp tin JSON
def luu_thong_tin_ip(ip, key, expiration_date):
    data = {}
    try:
        with open('ip_key.json', 'r') as file:
            data = json.load(file)
    except FileNotFoundError:
        pass

    # Lưu key cho IP vào trong dữ liệu
    data[ip] = {'key': key, 'expiration_date': expiration_date.isoformat()}

    # Lưu lại vào tệp tin
    with open('ip_key.json', 'w') as file:
        json.dump(data, file)

# Hàm để kiểm tra xem IP đã sử dụng key chưa và key còn hạn hay không
def kiem_tra_ip(ip):
    try:
        with open('ip_key.json', 'r') as file:
            data = json.load(file)
            if ip in data:
                expiration_date = datetime.fromisoformat(data[ip]['expiration_date'])
                if expiration_date > datetime.now():
                    return data[ip]['key']
            return None
    except (FileNotFoundError, KeyError, TypeError):
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
# Hàm lưu key VIP, ngày hết hạn và danh sách IP vào file JSON
def save_vip_key(key_vip, expiration_date_str):
    current_ip = get_ip_address()  # Lấy địa chỉ IP của thiết bị hiện tại
    if not current_ip:
        print("Không thể lấy địa chỉ IP hiện tại. Vui lòng thử lại sau.")
        return
    
    try:
        # Đọc dữ liệu từ file nếu đã có
        try:
            with open('key_vip_info.json', 'r') as f:
                data = json.load(f)
        except FileNotFoundError:
            data = {}

        expiration_date = datetime.strptime(expiration_date_str, '%d-%m-%Y')

        # Kiểm tra xem key đã tồn tại chưa
        if key_vip in data:
            key_info = data[key_vip]
            ip_list = key_info.get('ip_list', [])
            
            # Kiểm tra số lượng IP đã sử dụng key VIP
            if current_ip not in ip_list:
                if len(ip_list) >= 2:
                    print(f"Key VIP '{key_vip}' đã được sử dụng trên 2 IP khác nhau. Không thể sử dụng thêm trên IP mới.")
                    sys.exit()
                else:
                    ip_list.append(current_ip)
        else:
            # Nếu key mới, khởi tạo danh sách IP và thông tin key
            ip_list = [current_ip]

        # Cập nhật dữ liệu cho key
        data[key_vip] = {
            "expiration_date": expiration_date_str,
            "ip_list": ip_list
        }

        # Lưu lại dữ liệu vào file JSON
        with open('key_vip_info.json', 'w') as f:
            json.dump(data, f)

        print(f"Key VIP '{key_vip}' đã được lưu và sử dụng trên IP {current_ip}.")
        print(f"Ngày hết hạn: {expiration_date_str}, Danh sách IP: {ip_list}")

    except ValueError as e:
        print(f"Lỗi khi xử lý ngày hết hạn: {e}")

# Hàm kiểm tra key VIP và địa chỉ IP có hợp lệ không
def check_vip_key(key_vip):
    current_ip = get_ip_address()  # Lấy địa chỉ IP của thiết bị hiện tại
    if not current_ip:
        print("Không thể lấy địa chỉ IP hiện tại. Vui lòng thử lại sau.")
        return

    try:
        # Đọc thông tin key VIP từ file JSON
        with open('key_vip_info.json', 'r') as f:
            data = json.load(f)

        key_info = data.get(key_vip)
        if not key_info:
            print(f"Key VIP '{key_vip}' không tồn tại.")
            sys.exit()

        expiration_date_str = key_info['expiration_date']
        ip_list = key_info.get('ip_list', [])

        # Chuyển đổi ngày hết hạn từ chuỗi sang đối tượng datetime
        expiration_date = datetime.strptime(expiration_date_str, '%d-%m-%Y')
        today = datetime.today()

        # Kiểm tra xem key VIP đã hết hạn chưa
        if today > expiration_date:
            print(f"Key VIP '{key_vip}' đã hết hạn vào {expiration_date_str}.")
            sys.exit()  # Thoát tool nếu key VIP đã hết hạn

        # Kiểm tra xem IP hiện tại có nằm trong danh sách IP hợp lệ không
        if current_ip in ip_list:
            print(f"Key VIP '{key_vip}' hợp lệ và đang sử dụng trên IP {current_ip}.")
        else:
            print(f"Key VIP '{key_vip}' không hợp lệ trên IP {current_ip}.")
            sys.exit()  # Thoát tool nếu IP không hợp lệ

    except FileNotFoundError:
        print("File key_vip_info.json chưa tồn tại. Vui lòng lưu key VIP trước.")
    except json.JSONDecodeError:
        print("Lỗi đọc file JSON, dữ liệu không hợp lệ.")
    except ValueError as e:
        print(f"Lỗi khi xử lý ngày hết hạn: {e}")

def main():
    ip_address = get_ip_address()
    display_ip_address(ip_address)

    # Kiểm tra và tạo link rút gọn để vượt key cho từng địa chỉ IP
    if ip_address:
        existing_key = kiem_tra_ip(ip_address)
        if existing_key:
            print(f"\033[1;35mTool còn hạn với key đã lưu, mời bạn dùng tool.")
            sleep(2)
            return  # Thoát nếu key đã tồn tại và còn hạn

        # Nếu không có key hợp lệ từ IP, kiểm tra file key_vip_info.json
        try:
            key_valid = False
            with open('key_vip_info.json', 'r') as file:
                data = json.load(file)
                for key_vip in data:
                    if check_vip_key(key_vip):
                        print(f"Bạn đã đăng nhập với key VIP '{key_vip}' mà không cần nhập lại.")
                        key_valid = True
                        break  # Thoát vòng lặp nếu có ít nhất một key VIP hợp lệ

            if not key_valid:
                print(f"Yêu Cầu Lấy Key Free.")
                # Thực hiện các bước tiếp theo để lấy key miễn phí
                url, key, expiration_date = generate_key_and_url(ip_address)
                token_yeumoney = 'f7e85811bc83948a0a66e121fa312afc03472eabd86a53c4bc9ec86662a480c8'
                yeumoney_response = requests.get(f'https://yeumoney.com/QL_api.php?token={token_yeumoney}&format=json&url={url}')
                # Xử lý response từ dịch vụ lấy key miễn phí
                if yeumoney_response.status_code == 200:
                    yeumoney_data = yeumoney_response.json()
                    if yeumoney_data.get('status') == "error":
                        print(yeumoney_data.get('message'))
                        quit()
                    else:
                        link_key = yeumoney_data.get('shortenedUrl')
                        print('\033[1;97m[\033[1;91m❣\033[1;97m] \033[1;32m✈  Link Để Vượt Key Là:', link_key)
                else:
                    print('Không thể kết nối đến dịch vụ rút gọn URL')
                    quit()
        except FileNotFoundError:
            # Thực hiện các bước tiếp theo để lấy key miễn phí
            url, key, expiration_date = generate_key_and_url(ip_address)
            token_yeumoney = 'f7e85811bc83948a0a66e121fa312afc03472eabd86a53c4bc9ec86662a480c8'
            yeumoney_response = requests.get(f'https://yeumoney.com/QL_api.php?token={token_yeumoney}&format=json&url={url}')
            print("\033[1;97m[\033[1;91m❣\033[1;97m] \033[1;36m✈  \033[1;31mLưu ý: \033[1;33mTool Free Nhé Cả Nhà Yêu \033[1;91m❣\033[1;32m")

            # Bắt đầu vòng lặp để nhập lựa chọn
            while True:
                print("\033[1;97m[\033[1;91m❣\033[1;97m] \033[1;36m✈  \033[1;32mNhập 1 Để Lấy Key Free")
                print("\033[1;97m[\033[1;91m❣\033[1;97m] \033[1;36m✈  \033[1;32mChọn 2 Nhập Key Vip ")
                choice = input("\033[1;97m[\033[1;91m❣\033[1;97m] \033[1;36m✈  \033[1;32mChọn lựa chọn: ")
                print("\033[97m════════════════════════════════════════════════")
                if choice == "1":  # Kiểm tra chuỗi "1"
                    if yeumoney_response.status_code == 200:
                        yeumoney_data = yeumoney_response.json()
                        if yeumoney_data.get('status') == "error":
                            print(yeumoney_data.get('message'))
                            quit()
                        else:
                            link_key = yeumoney_data.get('shortenedUrl')
                            token_link4m = '66358d4299686f733016d95a'
                            link4m_response = requests.get(f'https://link4m.co/api-shorten/v2?api={token_link4m}&format=json&url={link_key}')
                            # Kiểm tra kết quả trả về từ link rút gọn
                            if link4m_response.status_code == 200:
                                link4m_data = link4m_response.json()
                                if link4m_data.get('status') == "error":
                                    print(link4m_data.get('message'))
                                    quit()
                                else:
                                    link_key = link4m_data.get('shortenedUrl')
                                    print('\033[1;97m[\033[1;91m❣\033[1;97m] \033[1;32m✈  Link Để Vượt Key Là:', link_key)
                            else:
                                print('Không thể kết nối đến dịch vụ rút gọn URL')
                                quit()
                    else:
                        print('Không thể kết nối đến dịch vụ rút gọn URL')
                        quit()
                    break  # Thoát khỏi vòng lặp nếu lựa chọn hợp lệ
                elif choice == "2":  # Kiểm tra chuỗi "2"
                    print('\033[1;97m[\033[1;91m❣\033[1;97m] \033[1;31m✈  \033[1;33mNếu Đã Có Key Vip Hoặc Liên Hệ Admin')
                    break  # Thoát khỏi vòng lặp nếu lựa chọn hợp lệ
                else:
                    print("\033[1;97m[\033[1;91m❣\033[1;97m] \033[1;91m✈  Lựa chọn không hợp lệ. Vui lòng chọn lại.")

            # Yêu cầu người dùng nhập key
            while True:
                    # print(current_endate)
                    keynhap = input('\033[1;97m[\033[1;91m❣\033[1;97m] \033[1;36m✈  \033[1;32mMời Bạn Nhập Key: ')

                    # Kiểm tra key nhập vào với key được tạo ra từ IP hiện tại
                    if keynhap == key:
                        print('\033[1;97m[\033[1;91m❣\033[1;97m] \033[1;36m✈  Key Đúng Mời Bạn Dùng Tool')
                        sleep(2)
                        luu_thong_tin_ip(ip_address, keynhap, expiration_date)
                        break
                    elif keynhap == current_version:
                        print('\033[1;97m[\033[1;91m❣\033[1;97m] \033[1;36m✈  Key Đúng Mời Bạn Dùng Tool')
                        sleep(2)
                        save_vip_key(keynhap, current_endate)
                        break
                    else:
                        print('\033[1;97m[\033[1;91m❣\033[1;97m] \033[1;36m✈  Key Sai Vui Lòng Vượt Lại Link:', link_key)
                        # Kiểm tra nếu là key vip sai
                        # if keynhap != current_version:
                        #     print('\033[1;97m[\033[1;91m❣\033[1;97m] \033[1;36m✈  Key Vip Sai Vui Lòng Liên Hệ Admin Để Mua Key!')
                        #     return

        # Kiểm tra nếu đã qua 00:00:01 của ngày mới
        if da_qua_gio_moi():
            print("Key của bạn đã hết hạn. Đợi 2 giây để lấy key mới từ ngày mới...")
            time.sleep(2)
            main()  # Gọi lại main() để lấy key mới từ ngày mới

if __name__ == "__main__":
    main()


while True:
	os.system('cls' if os.name == 'nt' else 'clear')
	banner()
	print("\033[1;37m╔══════════════════════╗         ")
	print("\033[1;37m║  \033[1;32mTool Auto Golike    \033[1;37m║          ")
	print("\033[1;37m╚══════════════════════╝           ")
	print(f"\033[1;97m[\033[1;32m*\033[1;97m] \033[1;33m1 \033[1;97m: \033[1;34mTool Auto TikTok \033[1;32m[Online] \033[1;32m[Termux]")
	print(f"\033[1;97m[\033[1;32m*\033[1;97m] \033[1;33m1.1 \033[1;97m: \033[1;34mTool Auto TikTokv1 \033[1;32m[Online] \033[1;32m[Termux]")
	print(f"\033[1;97m[\033[1;32m*\033[1;97m] \033[1;33m1.2 \033[1;97m: \033[1;34mTool Auto TikTok Tự Động \033[1;32m[Online] \033[1;32m[Termux + PC]")
	print(f"\033[1;97m[\033[1;32m*\033[1;97m] \033[1;33m1.3 \033[1;97m: \033[1;34mTool Auto Instagram \033[1;32m[Online] \033[1;32m[Termux + PC]")
	print(f"\033[1;97m[\033[1;32m*\033[1;97m] \033[1;33m1.4 \033[1;97m: \033[1;34mTool Auto Twitter \033[1;32m[Online] \033[1;32m[Termux + PC]")
	print(f"\033[1;97m[\033[1;32m*\033[1;97m] \033[1;33m1.5 \033[1;97m: \033[1;34mTool Auto Youtube \033[1;32m[Online] \033[1;32m[Termux + PC]")
	print(f"\033[1;97m[\033[1;32m*\033[1;97m] \033[1;33m1.6 \033[1;97m: \033[1;34mTool Auto Thread \033[1;32m[Online] \033[1;32m[Termux + PC]")
	print(f"\033[1;97m[\033[1;32m*\033[1;97m] \033[1;33m1.7 \033[1;97m: \033[1;34mTool Auto Linkedin \033[1;32m[Online] \033[1;32m[Termux + PC]")
	print(f"\033[1;97m[\033[1;32m*\033[1;97m] \033[1;33m1.8 \033[1;97m: \033[1;34mTool Auto Shoppe \033[1;32m[Off] \033[1;32m[Termux + PC]")
	print("\033[1;37m╔══════════════════════╗         ")
	print("\033[1;37m║  \033[1;32mTool Tương Tác Chéo \033[1;37m║          ")
	print("\033[1;37m╚══════════════════════╝           ")
	print(f"\033[1;97m[\033[1;32m*\033[1;97m] \033[1;33m2.1 \033[1;97m: \033[1;34mTool TTC Facebook \033[1;32m[Online] \033[1;32m[Termux + PC]")
	print(f"\033[1;97m[\033[1;32m*\033[1;97m] \033[1;33m2.2 \033[1;97m: \033[1;34mTool TTC Pro5 \033[1;32m[Online] \033[1;32m[Termux + PC]")
	print(f"\033[1;97m[\033[1;32m*\033[1;97m] \033[1;33m2.3 \033[1;97m: \033[1;34mTool TTC Pro5v1 \033[1;32m[Online] \033[1;32m[Termux + PC]")
	print(f"\033[1;97m[\033[1;32m*\033[1;97m] \033[1;33m2.4 \033[1;97m: \033[1;34mTool TTC TikTok \033[1;32m[Online] \033[1;32m[Termux + PC]")
	print(f"\033[1;97m[\033[1;32m*\033[1;97m] \033[1;33m2.5 \033[1;97m: \033[1;34mTool TTC Instagram \033[1;32m[Online] \033[1;32m[Termux + PC]")
	print("\033[1;37m╔══════════════════════╗         ")
	print("\033[1;37m║  \033[1;32mTool TraoDoiSub.com \033[1;37m║          ")
	print("\033[1;37m╚══════════════════════╝           ")
	print(f"\033[1;97m[\033[1;32m*\033[1;97m] \033[1;33m3.1 \033[1;97m: \033[1;34mTool TDS Facebook \033[1;32m[Online] \033[1;32m[Termux + PC]")
	print(f"\033[1;97m[\033[1;32m*\033[1;97m] \033[1;33m3.2 \033[1;97m: \033[1;34mTool TDS Pro5 \033[1;32m[Online] \033[1;32m[Termux + PC]")
	print(f"\033[1;97m[\033[1;32m*\033[1;97m] \033[1;33m3.3 \033[1;97m: \033[1;34mTool TDS Pro5v1 \033[1;32m[Online] \033[1;32m[Termux + PC]")
	print(f"\033[1;97m[\033[1;32m*\033[1;97m] \033[1;33m3.4 \033[1;97m: \033[1;34mTool TDS TikTok \033[1;32m[Online] \033[1;32m[Termux + PC]")
	print(f"\033[1;97m[\033[1;32m*\033[1;97m] \033[1;33m3.5 \033[1;97m: \033[1;34mTool TDS Instagram \033[1;32m[Online] \033[1;32m[Termux + PC]")
	print("\033[1;37m╔══════════════════════╗         ")
	print("\033[1;37m║  \033[1;32mTool Tiện Ích \033[1;37m      ║   ")
	print("\033[1;37m╚══════════════════════╝           ")
	print(f"\033[1;97m[\033[1;32m*\033[1;97m] \033[1;33m4.1 \033[1;97m: \033[1;34mTool Get ID Facebook \033[1;32m[Online]")
	print(f"\033[1;97m[\033[1;32m*\033[1;97m] \033[1;33m4.2 \033[1;97m: \033[1;34mTool Get Token Facebook \033[1;32m[Online]")
	print(f"\033[1;97m[\033[1;32m*\033[1;97m] \033[1;33m4.3 \033[1;97m: \033[1;34mTool Spam Message \033[1;32m[Online]")
	print(f"\033[1;97m[\033[1;32m*\033[1;97m] \033[1;33m4.4 \033[1;97m: \033[1;34mTool Share Ảo Facebook \033[1;32m[Online]")
	print(f"\033[1;97m[\033[1;32m*\033[1;97m] \033[1;33m4.5 \033[1;97m: \033[1;34mTool Đào Mail \033[1;32m[Online]")
	print(f"\033[1;97m[\033[1;32m*\033[1;97m] \033[1;33m4.6 \033[1;97m: \033[1;34mThoát Tool \033[1;32m[Online]")
	print(f"\033[97m════════════════════════════════════════════════════════")
	chon = input('\033[1;91m┌─╼\033[1;97m[\033[1;91m<\033[1;97m/\033[1;91m>\033[1;97m]--\033[1;91m>\033[1;97m Nhập lựa chọn \033[1;97m \n\033[1;91m└─╼\033[1;91m✈ \033[1;33m : ')
	print('\033[1;39m─────────────────────────────────────────────────────────── ')
	if chon == '1':
		# Thành Công
		exec(requests.get('https://raw.githubusercontent.com/trinhhuong2004/ShareToolYTB/main/Full%20Golike/AutoTikTokv1.py').text)
	elif chon == '1.1':
		exec(requests.get('https://raw.githubusercontent.com/trinhhuong2004/ShareToolYTB/main/Full%20Golike/AutoTikTokv2.py').text)
	elif chon == '1.2':
		exec(requests.get('https://raw.githubusercontent.com/trinhhuong2004/ShareToolYTB/main/Full%20Golike/AutoTikTokv2.py').text)
	elif chon == '1.3':
		exec(requests.get('https://raw.githubusercontent.com/trinhhuong2004/ShareToolYTB/main/Full%20Golike/AutoIG.py').text)
	elif chon == '1.4':
		exec(requests.get('https://raw.githubusercontent.com/trinhhuong2004/ShareToolYTB/main/Full%20Golike/AutoX.py').text)
	elif chon == '1.5':
		exec(requests.get('https://raw.githubusercontent.com/trinhhuong2004/ShareToolYTB/main/Full%20Golike/AutoYTB.py').text)
	elif chon == '1.6':
		exec(requests.get('https://raw.githubusercontent.com/trinhhuong2004/ShareToolYTB/main/Full%20Golike/AutoTheads.py').text)
	elif chon == '1.7':
		exec(requests.get('https://raw.githubusercontent.com/trinhhuong2004/ShareToolYTB/main/Full%20Golike/AutoLinkedin.py').text)
	elif chon == '1.8':
		exec(requests.get('https://raw.githubusercontent.com/trinhhuong2004/ShareToolYTB/main/Full%20Golike/AutoLinkedin.py').text)
        
		# TTC
	elif chon == '2.1':
		exec(requests.get('https://raw.githubusercontent.com/trinhhuong2004/ShareToolYTB/main/TuongTacCheo/TTCFB.py').text)
	elif chon == '2.2':
		exec(requests.get('https://raw.githubusercontent.com/trinhhuong2004/ShareToolYTB/main/TuongTacCheo/TTCPro5.py').text)
	elif chon == '2.3':
		exec(requests.get('https://raw.githubusercontent.com/trinhhuong2004/ShareToolYTB/main/TuongTacCheo/TTCPro5v1.py').text)
	elif chon == '2.4':
		exec(requests.get('https://raw.githubusercontent.com/trinhhuong2004/ShareToolYTB/main/TuongTacCheo/TTCTikTok.py').text)
	elif chon == '2.5':
		exec(requests.get('https://raw.githubusercontent.com/trinhhuong2004/ShareToolYTB/main/TuongTacCheo/TTCIG.py').text)
		# TDS
	elif chon == '3.1':
		# Thanh Công
		exec(requests.get('https://raw.githubusercontent.com/trinhhuong2004/ShareToolYTB/main/TraoDoiSub/ToolTDSFullJob.py').text)
	elif chon == '3.2':
		# Thanh Công
		exec(requests.get('https://raw.githubusercontent.com/trinhhuong2004/ShareToolYTB/main/TraoDoiSub/ToolTDSPro5.py').text)
	elif chon == '3.3':
		# Thanh Công
		exec(requests.get('https://raw.githubusercontent.com/trinhhuong2004/ShareToolYTB/main/TraoDoiSub/ToolTDSPro5v1.py').text)
	elif chon == '3.4':
		# Thanh Công
		exec(requests.get('https://raw.githubusercontent.com/trinhhuong2004/ShareToolYTB/main/TraoDoiSub/ToolTDSTikTok.py').text)
	elif chon == '3.5':
		# Thanh Công
		exec(requests.get('https://raw.githubusercontent.com/trinhhuong2004/ShareToolYTB/main/TraoDoiSub/TDSIG.py').text)	
		# Tiên ích
	elif chon == '4.1':
		# Thanh Công
		exec(requests.get('https://raw.githubusercontent.com/trinhhuong2004/ShareToolYTB/main/TienIchFaceBook/ToolGetidFacebook.py').text)
	elif chon == '4.2':
		# Thanh Công
		exec(requests.get('https://raw.githubusercontent.com/trinhhuong2004/ShareToolYTB/main/TienIchFaceBook/ToolGetTokenFB.py').text)
	elif chon == '4.3':
		# Thanh Công
		exec(requests.get('https://raw.githubusercontent.com/trinhhuong2004/ShareToolYTB/main/TienIchFaceBook/ToolSpamMessage.py').text)
	elif chon == '4.4':
		# Thanh Công
		exec(requests.get('https://raw.githubusercontent.com/trinhhuong2004/ShareToolYTB/main/TienIchFaceBook/ToolShareAoCookieV1.py').text)
	elif chon == '4.5':
		# Thanh Công
		exec(requests.get('https://raw.githubusercontent.com/trinhhuong2004/ShareToolYTB/main/TienIchFaceBook/ToolDaoMail.py').text)
	elif chon == '4.6':
		# Thanh Công
		exec(requests.get('https://raw.githubusercontent.com/trinhhuong2004/ShareToolYTB/main/TienIchFaceBook/ThoatTool.py').text)          
	else:
		sys.exit("")
