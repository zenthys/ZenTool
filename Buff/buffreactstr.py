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
# Đánh Dấu Bản Quyền
ndp_tool = "\033[1;97m[\033[1;91m❣\033[1;97m] \033[1;36m✈  "
ndp = "\033[1;97m[\033[1;91m❣\033[1;97m] \033[1;36m✈  "
# Config
dem = 0
# PHẦN LIST
listcx = []
list_page_pro5 = []
# import lib
import os,sys,requests,threading
from time import sleep
from datetime import datetime
try:
    import requests
except:
    print(luc+"Bạn Chưa Tải Thư Viện \n Bắt Đầu Tải... ")
    os.system("pip install requests")
# ====================== [ FUNCTION ] ======================
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
os.system("cls" if os.name == "nt" else "clear")
def echo(a):
   for i in range(len(a)):
     sys.stdout.write(a[i])
     sys.stdout.flush()
     sleep(0.00)
   print()
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
\033[1;97m[\033[1;91m❣\033[1;97m]\033[1;97m Tool   \033[1;31m  : \033[1;97m☞ \033[1;31mBuff Reaction Story Bằng Page Pro5♔ \033[1;97m☜
\033[1;97m[\033[1;91m❣\033[1;97m]\033[1;97m Tik Tok\033[1;31m  : \033[1;33mhttps:\033[1;32m//www.tiktok.com\033[1;31m/m@huongdev27
\033[1;97m[\033[1;91m❣\033[1;97m]\033[1;97m Zalo\033[1;31m     : \033[1;97m☞\033[1;31m0\033[1;37m3\033[1;36m6\033[1;35m2\033[1;34m1\033[1;33m6\033[1;33m6\033[1;34m8\033[1;35m6\033[1;37m3☜
\033[1;97m[\033[1;91m❣\033[1;97m]\033[1;97m Facebook\033[1;31m : \033[1;97mi.urs.bin.python.TrinhHuong 
\033[1;97m[\033[1;91m❣\033[1;97m]\033[1;97m Telegram\033[1;31m : \033[1;97m☞\033[1;32mhttps://t.me/+77MuosyD-yk4MGY1🔫\033[1;97m☜
\033[97m════════════════════════════════════════════════
\033[1;97m[\033[1;91m❣\033[1;97m]\033[1;97m Youtube\033[1;31m  : \033[1;97m☞ \033[1;36mHướng Dev - Kiếm Tiền Online\033[1;31m♔ \033[1;97m☜
╯"""
    echo(banner)
def clear():
    os.system("cls" if os.name == "nt" else "clear")
def thanh():
    print('\033[1;37m- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -')
def ndp_delay(o):
    while(o>1):
        o=o-1
        print(f'{trang}[\033[1;31mH\033[1;33muo\033[1;36mng\033[1;35mD\033[1;34me\033[1;32mv\033[1;37m[\033[1;36m|\033[1;37m]\033[1;37m[.....]\033[1;37m[{o}]','     ',end='\r');sleep(1/6)
        print(f'{trang}[\033[1;31mH\033[1;33muo\033[1;36mng\033[1;35mD\033[1;34me\033[1;32mv\033[1;37m[\033[1;31m/\033[1;37m]\033[1;37m[\033[1;32m>\033[1;37m....]\033[1;37m[{o}]','     ',end='\r');sleep(1/6)
        print(f'{trang}[\033[1;31mH\033[1;33muo\033[1;36mng\033[1;35mD\033[1;34me\033[1;32mv\033[1;37m[\033[1;32m-\033[1;37m]\033[1;37m[\033[1;32m>\033[1;31m>\033[1;37m...]\033[1;37m[{o}]','     ',end='\r');sleep(1/6)
        print(f'{trang}[\033[1;31mH\033[1;33muo\033[1;36mng\033[1;35mD\033[1;34me\033[1;32mv\033[1;37m[\033[1;33m+\033[1;37m]\033[1;37m[\033[1;32m>\033[1;31m>\033[1;36m>\033[1;37m..]\033[1;37m[{o}]','     ',end='\r');sleep(1/6)
        print(f'{trang}[\033[1;31mH\033[1;33muo\033[1;36mng\033[1;35mD\033[1;34me\033[1;32mv\033[1;37m[\033[1;34m\{trang}]\033[1;37m[\033[1;32m>\033[1;31m>\033[1;36m>\033[1;33m>\033[1;37m.]\033[1;37m[{o}]','     ',end='\r');sleep(1/6)
        print(f'{trang}[\033[1;31mH\033[1;33muo\033[1;36mng\033[1;35mD\033[1;34me\033[1;32mv\033[1;37m[\033[1;35m|\033[1;37m]\033[1;37m[\033[1;32m>\033[1;31m>\033[1;36m>\033[1;33m>\033[1;35m>\033[1;37m]\033[1;37m[{o}]','     ',end='\r');sleep(1/6)
def tangcxstr(x, dem, linkstr, dataurlstr):
    camxuc = listcx[0]
    time = datetime.now().strftime("%H:%M:%S")
    uid_page = list_page_pro5[x].split('|')[0]
    name_page = list_page_pro5[x].split('|')[1]
    list1 = (f'i_user={uid_page};')
    cookie9 = (f'{cookie}{list1}')
    headers = {
        'authority': 'www.facebook.com',
        'accept': '*/*',
        'accept-language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
        'origin': 'https://www.facebook.com',
        'referer': linkstr,
        'sec-ch-prefers-color-scheme': 'light',
        'sec-ch-ua': '"Chromium";v="106", "Google Chrome";v="106", "Not;A=Brand";v="99"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36',
        'viewport-width': '1221',
        'x-fb-friendly-name': 'useStoriesSendReplyMutation',
        'x-fb-lsd': '4CR-snjduLBRfA-cdgjhg_',
        'cookie': cookie9,
    }

    data = {
        'av': uid_page,
        '__user': uid_page,
        '__a': '1',
        '__dyn': '7AzHxqU5a5Q1ryUbFuC0BVU98nwgU29zEdEc8co2qwJxS1Nw9m3y4o1DU2_CxS320om782Cwwwqo465o-cw5MKdwGxu782lwv89kbxS2218wc61axe3S1lwlE-UqwsUkxe2GewGwkUtxGm2SUbElxm0zK5pUfE2FBx_wHwfCm2Sq2-azo2NwkQ0z8c84qifxe3u362-2B0oobo8o',
        '__csr': 'gP4nezNiOqiaH9H5qlPP_vilnFSncKIJESBc_riHQiGRB_iIgRl3maBgy8mlXp9oLD-XggV8zhaGbLBCUnCx-eDAKm78pCxim2yfUoJ12UGcUC3au6UgG9K225opwyxG9wFgfFE4S0MEkwyxOfxK1fwqouw9G1RwPx-0Q82jwoU5C1Twai0d3w2MUvw1Jy3e05ro03l7w1JG01MRw0iY8W0I81bU1G81zE0hZxC0D8',
        '__req': 'r',
        '__hs': '19325.HYP:comet_pkg.2.1.0.2.1',
        'dpr': '1',
        '__ccg': 'GOOD',
        '__rev': '1006641324',
        '__s': 'vcrj03:a4aoft:01km45',
        '__hsi': '7171454504668598048',
        '__comet_req': '15',
        'fb_dtsg': fb_dtsg,
        'jazoest': jazoest,
        'lsd': '4CR-snjduLBRfA-cdgjhg_',
        '__aaid': '497084035286445',
        '__spin_r': '1006641324',
        '__spin_b': 'trunk',
        '__spin_t': '1669734368',
        'fb_api_caller_class': 'RelayModern',
        'fb_api_req_friendly_name': 'useStoriesSendReplyMutation',
        'variables': '{"input":{"attribution_id_v2":"StoriesCometSuspenseRoot.react,comet.stories.viewer,via_cold_start,1669734368520,55579,,","lightweight_reaction_actions":{"offsets":[0],"reaction":"'+str(camxuc)+'"},"message":"'+str(camxuc)+'","story_id":"'+str(dataurlstr)+'","story_reply_type":"LIGHT_WEIGHT","actor_id":"100088148974138","client_mutation_id":"2"}}',
        'server_timestamps': 'true',
        'doc_id': '4826141330837571',
    }

    runtanglikestr = requests.post('https://www.facebook.com/api/graphql/', headers=headers, data=data).text
    if 'data' in runtanglikestr:
        print('\033[1;31m[\033[0;93m'+str(dem)+'\033[1;31m] | \033[1;36m'+str(time)+' \033[1;31m| \033[0;93mSuccess \033[1;31m| \033[1;34m'+str(uid_page)+' \033[1;31m| \033[1;35m'+str(name_page)+' \033[1;31m| \033[1;37m'+str(camxuc)+' \033[1;31m| \033[1;37m'+str(dataurlstr)+' ')
    else:
        print('\033[1;31mTăng Cảm Xúc Thất Bại, Có Vẻ ACC Bạn Đã Bị Block!!')
# =================[ CLEAR + THÔNG SỐ ADMIN ]===========================
clear()
banner()
cookie = input(ndp_tool+luc+'Vui Lòng Nhập Cookie Chứa Page Pro5'+trang+': '+vang)
# GET fb_dtsg + jazoest
headers = {
        'authority': 'mbasic.facebook.com',
        'cache-control': 'max-age=0',
        'sec-ch-ua': '"Google Chrome";v="93", " Not;A Brand";v="99", "Chromium";v="93"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'upgrade-insecure-requests': '1',
        'origin': 'https://mbasic.facebook.com',
        'content-type': 'application/x-www-form-urlencoded',
        'user-agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-user': '?1',
        'sec-fetch-dest': 'document',
        'referer': 'https://mbasic.facebook.com/',
        'accept-language': 'en-US,en;q=0.9',
        'cookie': cookie,
}
    
try:
    print(ndp_tool+xduong+"Đang Check Live Cookie...", end="\r")
    find_data = requests.get("https://mbasic.facebook.com/", headers=headers).text
    fb_dtsg = find_data.split('<input type="hidden" name="fb_dtsg" value="')[1].split('"')[0]
    jazoest = find_data.split('<input type="hidden" name="jazoest" value="')[1].split('"')[0]
except:
    exit(ndp_tool+do+"Cookie Die Vui Lòng Kiểm Tra Lại!!!")

# get id + name page
headers_getid = {
    'cookie': cookie, 
}
data = {
    'fb_dtsg': fb_dtsg,
    'jazoest': jazoest,
    'variables': '{"showUpdatedLaunchpointRedesign":true,"useAdminedPagesForActingAccount":false,"useNewPagesYouManage":true}',
    'doc_id': '5300338636681652'
}
getidpro5 = requests.post('https://www.facebook.com/api/graphql/', headers = headers_getid, data = data).json()['data']['viewer']['actor']['profile_switcher_eligible_profiles']['nodes']

for i in getidpro5:
    uid_page = i['profile']['id']
    name_page = i['profile']['name']
    gomlist = f'{uid_page}|{name_page}'
    list_page_pro5.append(gomlist)
# NHẬP THÔNG SỐ ĐỂ CHẠY TOOL
clear()
banner()
print(ndp_tool+luc+'GET THÀNH CÔNG'+trang+': '+str(len(list_page_pro5))+lam+' Page Pro5')
thanh()
linkstr = input(ndp_tool+trang+'Vui Lòng Nhập Link Story'+trang+': '+vang)
# TÁCH DATA TRONG URL STR
dataurlstr = linkstr.split('/')[5].split('/?')[0]
# GET THÀNH CÔNG
thanh()
print(ndp_tool+do+'['+vang+'SUCCESS'+do+']'+trang+': '+xduong+'ID STORY CỦA BẠN LÀ'+trang+': '+trang+str(dataurlstr)+'')
thanh()
# NHẬP CẢM XÚC
print(ndp_tool+luc+'Nhập Số '+do+'['+vang+'1'+do+'] '+trang+'Để Tăng Cảm Xúc '+hong+'Like')
print(ndp_tool+luc+'Nhập Số '+do+'['+vang+'2'+do+'] '+trang+'Để Tăng Cảm Xúc '+hong+'Love')
print(ndp_tool+luc+'Nhập Số '+do+'['+vang+'3'+do+'] '+trang+'Để Tăng Cảm Xúc '+hong+'Care')
print(ndp_tool+luc+'Nhập Số '+do+'['+vang+'4'+do+'] '+trang+'Để Tăng Cảm Xúc '+hong+'Haha')
print(ndp_tool+luc+'Nhập Số '+do+'['+vang+'5'+do+'] '+trang+'Để Tăng Cảm Xúc '+hong+'Wow')
print(ndp_tool+luc+'Nhập Số '+do+'['+vang+'6'+do+'] '+trang+'Để Tăng Cảm Xúc '+hong+'Sad')
print(ndp_tool+luc+'Nhập Số '+do+'['+vang+'7'+do+'] '+trang+'Để Tăng Cảm Xúc '+hong+'Angry')
thanh()
cx = int(input(ndp_tool+trang+'Vui Lòng Nhập Lựa Chọn'+trang+': '+vang))
if cx == 1:
    listcx.append('👍')
if cx == 2:
    listcx.append('❤️')
if cx == 3:
    listcx.append('🤗')
if cx == 4:
    listcx.append('😆')
if cx == 5:
    listcx.append('😮')
if cx == 6:
    listcx.append('😢')
if cx == 7:
    listcx.append('😡')
thanh()
soluongcx = int(input(ndp_tool+trang+'Nhập Số Lượng Cảm Xúc Cần Tăng'+trang+': '+vang))
thanh()
delay = int(input(ndp_tool+trang+'Vui Lòng Nhập Delay Tăng Cảm Xúc'+trang+': '+vang))
thanh()
while True:
    for x in range(int(len(list_page_pro5))):
        dem=dem+1
        threading.Thread(target=tangcxstr,args=(x, dem, linkstr, dataurlstr, )).start()
        ndp_delay(delay)
        if dem == soluongcx:
            thanh()
            exit(ndp_tool+luc+'Đã Hoàn Thành '+trang+str(soluongcx)+lam+' Cảm Xúc ')
            thanh()