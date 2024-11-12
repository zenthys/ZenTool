#Code By Nguyễn Hoàng Nam
import requests
import re
import threading
import random
import json
import os
import time
import sys
from colorama import Fore, Style, init

# -----[MÀU VÀ BIẾN]-----#
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
dac_biet = "\033[32;5;245m\033[1m\033[38;5;39m"
kt_code = "</>"
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
from time import sleep
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
dem = 0
print(f"Tiến hành kiểm tra toàn vẹn của file....")
def download_resource(url, file_path):
    response = requests.get(url)
    if response.status_code == 200:
        with open(file_path, "wb") as file:
            file.write(response.content)
        print(f"Tải về thành công: {file_path}")
    else:
        print(f"Lỗi khi tải về tài nguyên từ: {url}")

# Đường dẫn đến thư mục chứa các tệp tải về
resource_dir = "HuongDev"

# Kiểm tra và tải về file "config.json"
config_url = "https://namtool131.000webhostapp.com/emoji.json"
config_file_path = os.path.join(resource_dir, "emoji.json")
if not os.path.exists(config_file_path):
    os.makedirs(resource_dir, exist_ok=True)
    download_resource(config_url, config_file_path)
else:
    print(f"File đã tồn tại: {config_file_path}")
# -----[BẮT ĐẦU]-----#
init(convert=True)
System.Clear()
print(f"""
\033[1;33m██      ██╗      ████████╗ █████╗  █████╗ ██╗
\033[1;35m██╗    ╔██║      ╚══██╔══╝██╔══██╗██╔══██╗██║
\033[1;36m██║████║██║ █████╗  ██║   ██║  ██║██║  ██║██║
\033[1;37m██║    ╚██║ ╚════╝  ██║   ██║  ██║██║  ██║██║
\033[1;32m██║     ██║         ██║   ╚█████╔╝╚█████╔╝██████╗
\033[1;31m╚═╝     ╚═╝         ╚═╝    ╚════╝  ╚════╝ ╚═════╝\n
\033[1;97mTool By: \033[1;32mTrịnh Hướng            \033[1;97mPhiên Bản: \033[1;32m4.0     
\033[97m════════════════════════════════════════════════  
\033[1;97m[\033[1;91m❣\033[1;97m]\033[1;97m Tool   \033[1;31m  : \033[1;97m☞ \033[1;31mTool Follow Spam Comment♔ \033[1;97m☜
\033[1;97m[\033[1;91m❣\033[1;97m]\033[1;97m Tik Tok\033[1;31m  : \033[1;33mhttps:\033[1;32m//www.tiktok.com\033[1;31m/m@huongdev27
\033[1;97m[\033[1;91m❣\033[1;97m]\033[1;97m Zalo\033[1;31m     : \033[1;97m☞\033[1;31m0\033[1;37m3\033[1;36m6\033[1;35m2\033[1;34m1\033[1;33m6\033[1;33m6\033[1;34m8\033[1;35m6\033[1;37m3☜
\033[1;97m[\033[1;91m❣\033[1;97m]\033[1;97m Facebook\033[1;31m : \033[1;97mi.urs.bin.python.TrinhHuong 
\033[1;97m[\033[1;91m❣\033[1;97m]\033[1;97m Telegram\033[1;31m : \033[1;97m☞\033[1;32mhttps://t.me/+77MuosyD-yk4MGY1🔫\033[1;97m☜
\033[97m════════════════════════════════════════════════
\033[1;97m[\033[1;91m❣\033[1;97m]\033[1;97m Youtube\033[1;31m  : \033[1;97m☞ \033[1;36mHướng Dev - Kiếm Tiền Online\033[1;31m♔ \033[1;97m☜""")
cookies = input("\033[1;97m[\033[1;91m❣\033[1;97m] \033[1;36m✈  \033[1;32mVui Lòng Nhập Cookie Facebook: ")


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
\033[1;97m[\033[1;91m❣\033[1;97m]\033[1;97m Tool   \033[1;31m  : \033[1;97m☞ \033[1;31mTool Follow Spam Comment♔ \033[1;97m☜
\033[1;97m[\033[1;91m❣\033[1;97m]\033[1;97m Tik Tok\033[1;31m  : \033[1;33mhttps:\033[1;32m//www.tiktok.com\033[1;31m/m@huongdev27
\033[1;97m[\033[1;91m❣\033[1;97m]\033[1;97m Zalo\033[1;31m     : \033[1;97m☞\033[1;31m0\033[1;37m3\033[1;36m6\033[1;35m2\033[1;34m1\033[1;33m6\033[1;33m6\033[1;34m8\033[1;35m6\033[1;37m3☜
\033[1;97m[\033[1;91m❣\033[1;97m]\033[1;97m Facebook\033[1;31m : \033[1;97mi.urs.bin.python.TrinhHuong 
\033[1;97m[\033[1;91m❣\033[1;97m]\033[1;97m Telegram\033[1;31m : \033[1;97m☞\033[1;32mhttps://t.me/+77MuosyD-yk4MGY1🔫\033[1;97m☜
\033[97m════════════════════════════════════════════════
\033[1;97m[\033[1;91m❣\033[1;97m]\033[1;97m Youtube\033[1;31m  : \033[1;97m☞ \033[1;36mHướng Dev - Kiếm Tiền Online\033[1;31m♔ \033[1;97m☜"""



    for X in banner:
        sys.stdout.write(X)
        sys.stdout.flush()
        sleep(0.0000100)


os.system("clear")
os.system("cls")
banner()

count = 0
count_lock = threading.Lock()


def increment_count():
    global count
    with count_lock:
        count += 1


class FB:
    def __init__(self, cookies):
        self.headers = {
            "cookie": cookies,
            "Host": "d.facebook.com",
            "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
            "accept-language": "en-US,en;q=0.9",
            "cache-control": "max-age=0",
            "connection": "keep-alive",
            "sec-ch-ua-mobile": "?0",
            "sec-ch-ua": '"Microsoft Edge";v="117", "Not;A=Brand";v="8", "Chromium";v="117"',
            "sec-fetch-dest": "document",
            "sec-fetch-mode": "navigate",
            "sec-fetch-site": "none",
            "sec-fetch-user": "?1",
            "upgrade-insecure-requests": "1",
        }

    def comment(self, reply_id, id_post, c_user, comment):
        session = requests.Session()

        response = session.get("https://d.facebook.com/", headers=self.headers)
        data = response.text

        fb_dtsg = re.search(
            r'<input type="hidden" name="fb_dtsg" value="([^"]+)"', data
        ).group(1)
        jazoest = re.search(
            r'<input type="hidden" name="jazoest" value="([^"]+)"', data
        ).group(1)

        comment_data = {
            "fb_dtsg": fb_dtsg,
            "jazoest": jazoest,
            "comment_text": comment,
        }
        comment_headers = {
            **self.headers,
            "user-agent": "Mozilla/5.0 (Linux; Android 11; Pixel 5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.91 Mobile Safari/537.36 Edg/117.0.0.0",
        }
        response = session.post(
            f"https://d.facebook.com/a/comment.php?parent_comment_id={reply_id}&fs=0&comment_logging&ft_ent_identifier={id_post}&av={c_user}",
            data=comment_data,
            headers=comment_headers,
        )

        if response.status_code == 200:
            increment_count()
            return {"status": True, "data": "Comment Thành Công!"}
        else:
            return {"status": False, "data": "Comment Thất Bại!"}


def comment_on_post(cookies, reply_id, post_id, c_user, comment):
    increment_count()
    while True:
        action = FB(cookies)
        result = action.comment(reply_id, post_id, c_user, comment)
        with count_lock:
            current_count = count
            print(
                f"{Fore.GREEN}[ Nam~Dev ]{Style.RESET_ALL}: {current_count} | {result['data']} | {comment}"
            )

num_threads = int(input("\033[1;97m[\033[1;91m❣\033[1;97m] \033[1;36m✈  \033[1;32mNhập Số Luồng Muốn Chạy: "))
linkReply = input("\033[1;97m[\033[1;91m❣\033[1;97m] \033[1;36m✈  \033[1;32mVui Lòng Nhập Link Cần Spam: ")
postID = linkReply.split("ft_ent_identifier=")[1].split("&")[0]
parentCommentID = linkReply.split("ctoken=")[1].split("&")[0].split("_")[1]
cookie_pairs = cookies.split(";")
for pair in cookie_pairs:
    key, value = pair.strip().split("=")
    if key == "c_user":
        c_user_value = value
        break
print(
    "\033[1;96m- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -\n"
)
comment_text = ["Đừng Nhìn Cmt_", "Người Đẹp Trai Số 1 Thế Giới"]
with open(f"HuongDev/emoji.json", "r", encoding="utf-8") as json_file:
    data = json.load(json_file)
threads = []
for i in range(num_threads):
    thread = threading.Thread(
        target=comment_on_post,
        args=(
            cookies,
            parentCommentID,
            postID,
            c_user_value,
            random.choice(comment_text) + " " + random.choice(data),
        ),
    )
    threads.append(thread)
    thread.start()
