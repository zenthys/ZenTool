import requests
import time
import random
import os
# Mã màu sắc ANSI
XANH_LA = "\033[1;32m"  # Màu cho thông báo thành công
XANH_DUONG = "\033[1;34m"  # Màu cho thông báo xử lý
DO = "\033[1;31m"  # Màu cho thông báo lỗi
VANG = "\033[1;33m"  # Màu cho thông báo đang chờ
TRANG = "\033[1;37m"  # Màu trắng (dùng khi cần làm nổi bật)
KET_THUC = "\033[0m"  # Kết thúc màu



banner = f"""
\033[1;33m╔═══════════════════════════════════════════════╗
\033[1;33m║\033[1;35m██╗░░██╗██████╗██████═╗░██╗░░░░██░░░░██╗██████╗\033[1;33m║
\033[1;33m║\033[1;33m██║░░██║██░░░░║██░░░██╝░██║░░░░░██░░██╔╝██░░░░║\033[1;33m║
\033[1;33m║\033[1;39m███████║██████║██████╚╗░██║░░░░░░████╔╝░██████║\033[1;33m║
\033[1;33m║\033[1;36m██╔══██║██░░░░║██╔══██╚╗██║░░░░░░░██╔╝░░░░░░██║\033[1;33m║
\033[1;33m║\033[1;32m██║░░██║██████║██║░░░██║███████╗░░██║░░░██████║\033[1;33m║ 
\033[1;33m║\033[1;30m╚═╝░░╚═╝╚═════╝╚═╝░░░╚═╝╚══════╝░░╚═╝░░░╚═════╝\033[1;33m║ 
\033[1;33m║\033[1;30m░░░░╔██═╗░░╔███╗░░╔═██╗░░██═╗░░░██████═╗░░░░░░░\033[1;33m║ 
\033[1;33m║\033[1;31m░░░░╚╗██╚╗╔╝███╚╗╔╝██╔╝░████╚╗░░██░░░██╝░░░░░░░\033[1;33m║ 
\033[1;33m║\033[1;32m░░░░░╚╗██╚╝██░██╚╝██╔╝░██░░██╚╗░██████╚╗░░░░░░░\033[1;33m║ 
\033[1;33m║\033[1;33m░░░░░░╚╗████╔═╗████╔╝░████████╚╗██╔══██╚╗░░░░░░\033[1;33m║ 
\033[1;33m║\033[1;34m░░░░░░░╚╗██╔╝░╚╗██╔╝░██╔═════██║██║░░░██║░░░░░░\033[1;33m║ 
\033[1;33m║\033[1;35m░░░░░░░░╚══╝░░░╚══╝░░╚═╝░░░░░╚═╝╚═╝░░░╚═╝░░░░░░\033[1;33m║ 
\033[1;33m╠═══════════════════════════════════════════════╣
\033[1;33m║\033[1;34m▶ Nhóm Zalo  : \033[1;35mzalo.me/g/rbpywb976             \033[1;33m║
\033[1;33m║\033[1;34m▶ FaceBook : \033[1;35mfacebook.com/QuanHau210           \033[1;33m║
\033[1;33m║\033[1;34m▶ Zalo : \033[1;35m0961386638                            \033[1;33m║
\033[1;33m║\033[1;34m▶ Mua Key Vip Cứ Liên Hệ Zalo Nhé              \033[1;33m║
\033[1;33m║\033[1;34m▶ Nếu Có Lỗi Vui Lòng Báo Cho Facebook Nhé     \033[1;33m║
\033[1;33m╚═══════════════════════════════════════════════╝
\033[1;32m-------------------------------------------------"""
os.system('cls' if os.name == 'nt' else 'clear')
print(banner)
# Nhập danh sách tài khoản từ người dùng
list_acc = []
num_accounts = int(input(VANG + "\033[1;32mNhập số lượng tài khoản bạn muốn thêm: " + KET_THUC))

for i in range(num_accounts):
    username = input(f"\033[1;31m[\033[1;37m=.=\033[1;31m] \033[1;37m=> \033[1;32mNhập tài khoản {i+1} (username): " + KET_THUC)
    password = input(f"\033[1;31m[\033[1;37m=.=\033[1;31m] \033[1;37m=> \033[1;32mNhập mật khẩu {i+1} (password): " + KET_THUC)
    list_acc.append(f"{username}|{password}")

file_luu = "list_save.txt"
string_acc = ""

def delay(time_sec):
    for t in range(time_sec, 0, -1):
        print(f"\r{VANG}    Chờ sau {t} giây...    {KET_THUC}", end="")
        time.sleep(1)
    print()  # In dòng mới sau khi đếm thời gian

def check_user(cookie):
    url = 'https://traodoisub.com/view/setting/load.php'
    headers = {
        'authority': 'traodoisub.com',
        'accept': 'application/json, text/javascript, */*; q=0.01',
        'accept-language': 'vi-VN,vi;q=0.9,en;q=0.8',
        'cookie': cookie,
        'referer': 'https://traodoisub.com/view/setting/',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36',
        'x-requested-with': 'XMLHttpRequest'
    }

    response = requests.get(url, headers=headers)
    if '"tokentds":"' in response.text:
        return response.json()
    return False

def dang_nhap(username, password):
    url = 'https://traodoisub.com/scr/login.php'
    data = {
        'username': username,
        'password': password
    }
    headers = {
        'authority': 'traodoisub.com',
        'accept': 'application/json, text/javascript, */*; q=0.01',
        'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'referer': 'https://traodoisub.com/',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36',
        'x-requested-with': 'XMLHttpRequest'
    }

    response = requests.post(url, data=data, headers=headers, allow_redirects=False)
    if '"success":true' in response.text:
        cookie = response.headers.get('Set-Cookie').split(';')[0]
        return cookie
    return False

def doipass(cookie, old_password, new_password):
    url = 'https://traodoisub.com/scr/doipass.php'
    data = {
        'oldpass': old_password,
        'newpass': new_password,
        'renewpass': new_password
    }
    headers = {
        'cookie': cookie,
        'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'referer': 'https://traodoisub.com/view/setting/',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36',
        'x-requested-with': 'XMLHttpRequest'
    }

    response = requests.post(url, data=data, headers=headers)
    return response.text == "0"

def random_string(length):
    return ''.join(random.choice("qetyuiopadghklzcvbnmQETYUIOPA") for _ in range(length))

loi = 0
i1 = 0

for i, acc in enumerate(list_acc):
    if len(acc.strip()) < 5:
        loi += 1
        if loi > 3:
            break
        continue
    i1 += 1
    loi = 0

    username, password = acc.strip().split("|")
    
    print(XANH_LA + f"Đang xử lý tài khoản {i1}: {username}" + KET_THUC)

    print(VANG + "[\033[1;37m=.=\033[1;31m] Đang lấy cookie..." + KET_THUC)
    delay(1)
    cookie = dang_nhap(username, password)
    
    if cookie:
        print("[\033[1;37m=.=\033[1;31m] Đăng nhập thành công!" + KET_THUC)
        print(VANG + "[\033[1;37m=.=\033[1;31m] Đang kiểm tra user..." + KET_THUC)
        delay(1)
        check_user_data = check_user(cookie)
        
        if check_user_data:
            xu = check_user_data.get("xu")
            user = check_user_data.get("user")
            tokentds = check_user_data.get("tokentds")

            print("[\033[1;37m=.=\033[1;31m] Đang đổi pass cho " + username + "..." + KET_THUC)
            delay(1)
            new_password = "Herlys-" + random_string(8)
            if doipass(cookie, password, new_password):
                string_acc += f"{username}|{new_password}|{xu}|{tokentds}\n"
                with open(file_luu, "w") as f_save:
                    f_save.write(string_acc)
                print(XANH_LA + "[\033[1;37m=.=\033[1;31m] Đổi pass thành công cho " + username + ": " + new_password + KET_THUC)
                print(TRANG + f"[{username}|{new_password}] Tài khoản và mật khẩu mới cho {username} đã được ghi vào file." + KET_THUC)
            else:
                print("[\033[1;37m=.=\033[1;31m] Đổi pass thất bại cho " + username + KET_THUC)
        else:
            print("[\033[1;37m=.=\033[1;31m] Check user thất bại cho " + username + KET_THUC)
    else:
        print("[\033[1;37m=.=\033[1;31m] Tài khoản hoặc mật khẩu sai cho " + username + KET_THUC)
    
    delay(5)