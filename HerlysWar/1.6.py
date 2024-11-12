from urllib.parse import quote
import datetime
import os
import ssl
from urllib.parse import urlencode
from http import cookiejar
from urllib3.exceptions import InsecureRequestWarning
import hashlib
import random
try:
    import base64
    from requests.exceptions import RequestException
    import requests
    import pystyle
    from concurrent.futures import ThreadPoolExecutor
    from faker import Faker
    from requests import session
    import concurrent.futures
    
except ImportError:
    import os
    os.system("pip install faker")
    os.system("pip install colorama")
    os.system("pip install requests")
    os.system("pip install pystyle")
    os.system("pip install concurrent.futures")
    os.system("pip install base64")
import requests,os,time,re,json,uuid,random,sys
from concurrent.futures import ThreadPoolExecutor
import datetime
from datetime import datetime
import requests,json
import uuid
import requests
from time import sleep
from random import choice, randint, shuffle
from pystyle import Add, Center, Anime, Colors, Colorate, Write, System
from os.path import isfile
from pystyle import Colors, Colorate, Write, Center, Add, Box
from time import sleep,strftime
import socket
from pystyle import *

# fix
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')
    
def runbanner(text, delay=0.001):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()


trang = "\033[1;37m\033[1m"
xanh_la = "\033[1;32m\033[1m"
xanh_duong = "\033[1;34m\033[1m"
xanhnhat = '\033[1m\033[38;5;51m'
do = "\033[1;31m\033[1m\033[1m"
xam='\033[1;30m\033[1m'
vang = "\033[1;33m\033[1m"
tim = "\033[1;35m\033[1m"
hongnhat = "#FFC0CB"
kt_code = "</>"
dac_biet = "\033[32;5;245m\033[1m\033[38;5;39m"
colors = [
    "\033[1;37m\033[1m",  # Trắng
    "\033[1;32m\033[1m",  # Xanh lá
    "\033[1;34m\033[1m",  # Xanh dương
    "\033[1m\033[38;5;51m",  # Xanh nhạt
    "\033[1;31m\033[1m\033[1m",  # Đỏ
    "\033[1;30m\033[1m",  # Xám
    "\033[1;33m\033[1m",  # Vàng
    "\033[1;35m\033[1m",  # Tím
    "\033[32;5;245m\033[1m\033[38;5;39m",  # Màu đặc biệt
]
random_color = random.choice(colors)
def idelay(o):
    while(o>0):
        o=o-1
        print(f"{trang}[{do}</>{trang}] \033[1;33mV\033[1;34mu\033[1;35mi \033[1;32mL\033[1;33mò\033[1;34mn\033[1;35mg \033[1;36mC\033[1;33mh\033[1;34mờ {trang}[\033[1;35m.....""]""["+str(o)+"]""    ",end='\r')
        time.sleep(1/6)
        print(f"{trang}[{do}</>{trang}] \033[1;31mV\033[1;32mu\033[1;33mi \033[1;34mL\033[1;35mò\033[1;31mn\033[1;32mg \033[1;33mC\033[1;32mh\033[1;35mờ {trang}[\033[1;33m•{trang}....""]"f"{trang}[{xanhnhat}"+str(o)+f"{trang}]""     ",end='\r')
        time.sleep(1/6)
        print(f"{trang}[{do}</>{trang}] \033[1;32mV\033[1;33mu\033[1;34mi \033[1;35mL\033[1;36mò\033[1;33mn\033[1;34mg \033[1;35mC\033[1;31mh\033[1;32mờ {trang}[\033[1;35m••{trang}...""]"f"{trang}[{xanh_la}"+str(o)+f"{trang}]""     ",end='\r')
        time.sleep(1/6)
        print(f"{trang}[{do}</>{trang}] \033[1;31mV\033[1;33mu\033[1;35mi \033[1;33mL\033[1;31mò\033[1;32mn\033[1;34mg \033[1;36mC\033[1;35mh\033[1;31mờ {trang}[\033[1;32m•••{trang}..""]"f"{trang}[{do}"+str(o)+f"{trang}]""     ",end='\r')
        time.sleep(1/6)
        print(f"{trang}[{do}</>{trang}] \033[1;32mV\033[1;34mu\033[1;36mi \033[1;32mL\033[1;34mò\033[1;31mn\033[1;35mg \033[1;33mC\033[1;36mh\033[1;35mờ {trang}[\033[1;38m••••{trang}.""]"f"{trang}[{tim}"+str(o)+f"{trang}]""     ",end='\r')
        time.sleep(1/6)
        print(f"{xanhnhat}\033[1;37m[</>]\033[1;31mV\033[1;34mu\033[1;36mi \033[1;32mL\033[1;34mò\033[1;32mn\033[1;35mg \033[1;36mC\033[1;34mh\033[1;32mờ {trang}[\033[1;33m•••••{trang}""]"f"{trang}[{vang}"+str(o)+f"{trang}]""     ",end='\r')
        time.sleep(0.1)
        print(f"{trang}[{do}</>{trang}] \033[1;31mV\033[1;34mu\033[1;36mi \033[1;32mL\033[1;34mò\033[1;32mn\033[1;35mg \033[1;36mC\033[1;34mh\033[1;32mờ {trang}[\033[1;33m•••••{trang}""]"f"{trang}[{xanh_la}"+str(o)+f"{trang}]""     ",end='\r')

chontool = f"""
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
clear()
runbanner(chontool)
idcanspam=input(f'{trang}[{do}</>{trang}] \033[1;32m\033[1mID Box Cần Nhây Icon :{vang} ')
while True:
      ck=input(f'\033[1;97m[\033[1;31m</>\033[1;97m] {xanhnhat}Nhập Cookie Facebook :{vang} ')
      try:
        get=requests.get(f'https://mbasic.facebook.com/privacy/touch/block/confirm/?bid={idcanspam}&ret_cancel&source=profile',headers={'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','accept-language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5','cookie': ck,'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="102", "Google Chrome";v="102"','sec-ch-ua-mobile': '?0','sec-ch-ua-platform': '"Windows"','sec-fetch-dest': 'document','sec-fetch-mode': 'navigate','sec-fetch-site': 'same-origin','sec-fetch-user': '?1','upgrade-insecure-requests': '1'}).text
        fb_dtsg=get.split('<input type="hidden" name="fb_dtsg" value="')[1].split('" autocomplete="off" />')[0]
        jazoest=get.split('<input type="hidden" name="jazoest" value="')[1].split('" autocomplete="off" />')[0]
        clear()
        break
      except:
        print(f'{do}Cookie Sai!!')   
params = {
      "icm": '1',
    }
    
headers = {
      "Host":"mbasic.facebook.com",
      "content-length":"247",
      "content-type":"application/x-www-form-urlencoded",
      "user-agent":"Mozilla/5.0 (Linux; Android 8.1.0; Redmi 5A Build/OPM1.171019.026) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.5735.130 Mobile Safari/537.36",
      "accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
      "sec-fetch-site":"same-origin",
      "sec-fetch-mode":"navigate",
      "sec-fetch-user":"?1",
      "sec-fetch-dest":"document",
      "accept-encoding":"gzip, deflate, br",
      "accept-language":"vi-VN,vi;q=0.9,en-US;q=0.8,en;q=0.7",
      "cookie":ck,
    }
runbanner(chontool)
chon_name = str(input(f"{vang}Điền Icon Cần Treo {trang}: "))
if chon_name.lower() == "{chon_name}":
      lag = "{chon_name}"
elif chon_name.lower() == "ndjjdkd":
      lag = " "
else:
      CAU_CHUI = [
f"sao kia{chon_name}",
f"manh di ma{chon_name}",
f"kem ak{chon_name}",
f"sao kia{chon_name}",
f"son de{chon_name}",
f"run ak{chon_name}",
f"thg an hai{chon_name}",
f"cay tao ak{chon_name}",
f"cay lam ak{chon_name}",
f"sao roi nhi{chon_name}",
f"bat luc ak{chon_name}",
f"lien tuc de{chon_name}",
f"tiep de m{chon_name}",
f"nhay keo k e{chon_name}",
f"ga vay e{chon_name}",
f"hoc lom ak{chon_name}",
f"ko slow ma{chon_name}",
f"speed de{chon_name}",
f"hai vai l{chon_name}",
f"m dot ak{chon_name}",
f"thg oc cut{chon_name}",
f"chay de{chon_name}",
f"chat le dei{chon_name}",
f"co len{chon_name}",
f"mo coi ak{chon_name}",
f"cay ak{chon_name}",
f"ccho cayya ak{chon_name}",
f"oc cac ak{chon_name}",
f"chay ak em{chon_name}",
f"sua mau dei{chon_name}",
f"sua le dei{chon_name}",
f"tk dot{chon_name}",
f"tk oc dai{chon_name}",
f"sua le de{chon_name}",
f"manh kg{chon_name}",
f"manh ma e{chon_name}",
f"man ma em{chon_name}",
f"tk dot{chon_name}",
f"ui mo coi{chon_name}",
f"sua lej9 dei{chon_name}",
f"oc loz ak{chon_name}",
f"tk boai ngu{chon_name}",
f"son dc kg{chon_name}",
f"oc trau ak{chon_name}",
f"le ma em{chon_name}",
f"hot nhay ma{chon_name}",
f" tk oc dai{chon_name}",
f"sua manh kg{chon_name}",
f"m bi ngu ak{chon_name}",
f"sua mau kg{chon_name}",
f"oc trau ak{chon_name}",
f"speed em{chon_name}",
f"le nun ma{chon_name}",
f"tk dot cut{chon_name}",
f"bi ngu ak{chon_name}",
f"son de em{chon_name}",
f"ccho dien{chon_name}",
f"nhanh vl ma{chon_name}",
f"tay ma em{chon_name}",
f"slow ak{chon_name}",
f"oc boai ak{chon_name}",
f"tk dot{chon_name}",
f" bia ngu ak{chon_name}",
f"sua le nun{chon_name}",
f"phat bieu le{chon_name}",
f"tk dot nay{chon_name}",
f"mo coi me ak{chon_name}",
f"tk ngu{chon_name}",
f"sao da{chon_name}",
f"anh man mak{chon_name}",
f"cay akk{chon_name}",
f"sua mauu{chon_name}",
f"sloww akk{chon_name}",
f"le em{chon_name}",
f"nhanh em{chon_name}",
f"clmkks{chon_name}",
f"con cho dien{chon_name}",
f"sua em{chon_name}",
f"speed ma{chon_name}",
f"m slow ay{chon_name}",
f"m slow vl{chon_name}",
f"anh speed vkl{chon_name}",
f"le em{chon_name}",
f"clm ngu ak{chon_name}",
f"tk ga nay{chon_name}",
f"con loz{chon_name}",
f"sua le lun em{chon_name}",
f"clm dot ak{chon_name}",
f"keo man cai{chon_name}",
f"man off mxh de{chon_name}",
f"kg dam ak{chon_name}",
f"tk ngu ren{chon_name}",
f"cay r ak{chon_name}",
f"cay cmnr{chon_name}",
f"m cay ro{chon_name}",
f"nhanh ti{chon_name}",
f"le len e{chon_name}",
f"co de{chon_name}",
f"sap dc r{chon_name}",
f"co gang em{chon_name}",
f"bat luc r ak{chon_name}",
f"ui tk ga{chon_name}",
f"ga bat luc{chon_name}",
f"duoi r ak{chon_name}",
f"moi tay ak{chon_name}",
f"kakakak{chon_name}",
f"sua le nun{chon_name}",
f"chill ma{chon_name}",
f"bth ma em{chon_name}",
f"m bat on ak{chon_name}",
f"anh dg chill{chon_name}",
f"sua manh em{chon_name}",
f"kg dc treo nha{chon_name}",
f"tay vs bo de{chon_name}",
f"cn boai{chon_name}",
f"nao cho ak{chon_name}",
f"clm{chon_name}",
f"sua mau de{chon_name}",
f"ga ak m{chon_name}",
f"slow r ak m{chon_name}",
f"duoi r ak{chon_name}",
f"kh nghi ngoi{chon_name}",
f"lien tuc ma{chon_name}",
f"lien tuc nun{chon_name}",
f"chat lien tuc{chon_name}",
f"le kja m{chon_name}",
f"sao roi{chon_name}",
f"dien dai ak{chon_name}",
f"le len cmm{chon_name}",
f"so t ak{chon_name}",
f"clm dot ak{chon_name}",
f"anh kg bt duoi{chon_name}",
f"le ma em{chon_name}",
f"sua de{chon_name}",
f"tk dot nay{chon_name}",
f"le me ak{chon_name}",
f"tk oc bo{chon_name}",
f"loan phim r ak{chon_name}",
f"oc cho{chon_name}",
f"kay roi ak{chon_name}",
f"le de m{chon_name}",
f"clm ga l{chon_name}",
f"man off kg{chon_name}",
f"kay ak em{chon_name}",
f"tk oc l{chon_name}",
f"le len{chon_name}",
f"lien tuc ma{chon_name}",
f"slow kia{chon_name}",
f"oc ak{chon_name}",
f"cayy r{chon_name}",
f"muon win ak{chon_name}",
f"dot s win{chon_name}",
f"kakakk{chon_name}",
f"yeu akk may{chon_name}",
f"nhanh ma{chon_name}",
f"speed vl ayh nhi{chon_name}",
f"z ha m{chon_name}",
f"m dot ak{chon_name}",
f"m dot ma e{chon_name}",
f"tk dot kakka{chon_name}",
f"FaceBook : Quan Hau{chon_name}",
f"slow v{chon_name}",
f"le hon de{chon_name}",
f"lofi lun{chon_name}",
f"ui ga{chon_name}",
f"cay rui ak{chon_name}",
f"lien tuc de{chon_name}",
f"yeu v ak{chon_name}",
f"manh hon di{chon_name}",
f"kg dc ak{chon_name}",
f"oc cho ak{chon_name}",
f"sua lien tuc ma{chon_name}",
f"clm tk dot{chon_name}",
f"lien tuc nao{chon_name}",
f"sao roi m{chon_name}",
f"slow v ak{chon_name}",
f"ngu ak em{chon_name}",
f"tk dot dai cho{chon_name}",
]
      clear()
      runbanner(chontool)
      delay=int(input(f'\033[1;97m[\033[1;31m</>\033[1;97m] {xanhnhat}Nhập delay(Khuyến Cáo Trên 2) :{vang} '))
      while True:
        try:
          ping = requests.get("https://www.google.com")
          if ping.status_code == 200:
            for nd in CAU_CHUI:
                data = f"fb_dtsg={fb_dtsg}&jazoest={jazoest}&body={nd}&send=Send&tids=cid.g.{idcanspam}&wwwupp=C3&platform_xmd=&referrer=&ctype=&cver=legacy&csid=366a74a7-2d30-45dd-94c2-ad47d662dcfb"  
                response = requests.post("https://mbasic.facebook.com/messages/send/", params=params, headers=headers, data=data.encode('utf-8'))
                chonname = chon_name
                NOIDUNG = f"\033[1;35mĐã Gửi Thành Công\033[1;31m : \033[1;97m{nd}"
                print(f"{NOIDUNG}")
                idelay(delay)
        except Exception as e:
          print(f"{do}Lỗi bị ngắt kết lối vui lòng kết lối lại mạng để tiếp tục nhây")
          time.sleep(5)