import requests
import os

# Định nghĩa màu sắc cho đầu ra
trang = "\033[1;37m\033[1m"
xanh_la = "\033[1;32m\033[1m"
vang = "\033[1;33m\033[1m"

hack = "\033[1;31m[\033[1;37m=.=\033[1;31m] \033[1;37m=> "
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

def shorten_link(url):
    token = "59453dd758f1811e25bbd7ca15860e3a5695d5f61264b572384eadc6bd273e2c"
    api_url = f"https://yeumoney.com/QL_api.php?token={token}&format=text&url={url}"

    response = requests.get(api_url)

    if response.status_code == 200:
        return response.text  # Dữ liệu trả về là dạng text
    else:
        return "Error: " + str(response.status_code) + " - " + response.text

# Sử dụng tool
link = input(f"{hack}NHẬP LINK CẦN RÚT GỌN : {vang}")

# Rút gọn URL với API link4m.co
token_link1s = '6685a9375cd7941ad61c38f7'
response = requests.get(f'https://link4m.co/api-shorten/v2?api={token_link1s}&url={link}').json()

if response.get('status') == "error":
    print(f"Lỗi: {response.get('message')}")
else:
    shortened_link = response.get('shortenedUrl')
    print(f"{hack}{xanh_la}LINK RÚT GỌN CỦA BẠN LÀ: {vang}{shortened_link}")