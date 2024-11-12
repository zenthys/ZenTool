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
\033[1;33m║\033[1;34m▶ Nhóm Zalo  : \033[1;35mhttps://zalo.me/g/azfjwi735     \033[1;33m║
\033[1;33m║\033[1;34m▶ FaceBook : \033[1;35mhttps://bom.so/tZxIW6             \033[1;33m║
\033[1;33m║\033[1;34m▶ Zalo : \033[1;35mhttps://bom.so/wnhs5C                 \033[1;33m║
\033[1;33m║\033[1;34m▶ Mua Key Vip Cứ Liên Hệ Zalo Nhé              \033[1;33m║
\033[1;33m╚═══════════════════════════════════════════════╝
\033[1;32m-------------------------------------------------"""
clear()
runbanner(chontool)
idcanspam=input(f'\033[1;97m[\033[1;31m</>\033[1;97m] {xanhnhat}ID Box Cần Nhây :{vang} ')
while True:
      ck=input(f'\033[1;97m[\033[1;31m</>\033[1;97m] {xanhnhat}Nhập Cookie Facebook :{vang} ')
      try:
        get=requests.get(f'https://mbasic.facebook.com/privacy/touch/block/confirm/?bid={idcanspam}&ret_cancel&source=profile',headers={'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','accept-language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5','cookie': ck,'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="102", "Google Chrome";v="102"','sec-ch-ua-mobile': '?0','sec-ch-ua-platform': '"Windows"','sec-fetch-dest': 'document','sec-fetch-mode': 'navigate','sec-fetch-site': 'same-origin','sec-fetch-user': '?1','upgrade-insecure-requests': '1'}).text
        fb_dtsg=get.split('<input type="hidden" name="fb_dtsg" value="')[1].split('" autocomplete="off" />')[0]
        jazoest=get.split('<input type="hidden" name="jazoest" value="')[1].split('" autocomplete="off" />')[0]
        clear()
        break
      except:
        print(f'{do}Cookie sai!!')   
        runbanner(chontool)

params = {
      "icm": '1',
    }
    
headers = {
      "Host":"mbasic.facebook.com",
      "content-length":"87",
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
CAU_CHUI = [
"sao kia", "manh di ma", "kem ak", "sao kia", "son de", "run ak", "thg an hai","cay tao ak", "cay lam ak", "sao roi nhi", "bat luc ak", "lien tuc de", "tiep de m","nhay keo k e", "ga vay e", "hoc lom ak", "ko slow ma","speed de", "hai vai l","m dot ak", "thg oc cut", "chay de", "chat le dei", "co len", "mo coi ak", "cay ak", "ccho cayya ak", "oc cac ak", "chay ak em", "sua mau dei", "sua le dei", "tk dot", "tk oc dai", "sua le de", "manh kg", "manh ma e", "man ma em", "tk dot", "ui mo coi", "sua lej9 dei", "oc loz ak", "tk boai ngu", "son dc kg", "oc trau ak", "le ma em", "hot nhay ma", " tk oc dai", "sua manh kg", "m bi ngu ak", "sua mau kg", "oc trau ak", "speed em", "le nun ma", "tk dot cut", "bi ngu ak", "son de em", "ccho dien", "nhanh vl ma", "tay ma em", "slow ak", "oc boai ak", "tk dot", " bia ngu ak", "sua le nun", "phat bieu le", "tk dot nay", "mo coi me ak", "tk ngu", "sao da", "anh man mak", "cay akk", "sua mauu", "sloww akk", "le em", "nhanh em", "clmkks", "con cho dien", "sua em", "speed ma", "m slow ay", "m slow vl", "anh speed vkl", "le em", "clm ngu ak", "tk ga nay", "con loz", "sua le lun em", "clm dot ak", "keo man cai", "man off mxh de", "kg dam ak", "tk ngu ren", "cay r ak", "cay cmnr", "m cay ro", "nhanh ti", "le len e", "co de", "sap dc r", "co gang em", "bat luc r ak", "ui tk ga", "ga bat luc", "duoi r ak", "moi tay ak", "kakakak", "sua le nun", "chill ma", "bth ma em", "m bat on ak", "anh dg chill", "sua manh em", "kg dc treo nha", "tay vs bo de", "cn boai", "nao cho ak", "clm", "sua mau de", "ga ak m", "slow r ak m", "duoi r ak", "kh nghi ngoi", "lien tuc ma", "lien tuc nun", "chat lien tuc", "le kja m", "sao roi", "dien dai ak", "le len cmm", "so t ak", "clm dot ak", "anh kg bt duoi", "le ma em", "sua de", "tk dot nay", "le me ak", "tk oc bo", "loan phim r ak", "oc cho", "kay roi ak", "le de m", "clm ga l", "man off kg", "kay ak em", "tk oc l", "le len", "lien tuc ma", "slow kia", "oc ak", "cayy r", "muon win ak", "dot s win", "kakakk", "yeu akk may", "nhanh ma", "speed vl ayh nhi", "z ha m", "m dot ak", "m dot ma e", "tk dot kakka", "🤣🤣", "slow v", "le hon de", "lofi lun", "ui ga", "cay rui ak", "lien tuc de", "yeu v ak", "manh hon di", "kg dc ak", "oc cho ak", "sua lien tuc ma", "clm tk dot", "lien tuc nao", "sao roi m", "slow v ak", "ngu ak em", "tk dot dai cho", "liec tuc de m", "Sua lien tuc", "ko dc ak", "clm slow v", "nhanh ti dc kg", "cut tay ak", "tk ngheo", "m te nan ak", "phe ak", "co gang", "sap dc r", "ti nx di m", "speed xiu nx", "sap dc r do", "ga v ak", "sao doa kaka", "m ngu ak", "m dot ro", "tk oc dai", "oc trau ak", "cmm dot the", "man ma m", "manh nun ma", "tk dot slow v", "cay r ak", "sua de m", "lofi ma m", "sua chill v", "tk ga âkkak", "le de m", "Chill z", "sua lien tuc", "m that hoc ak", "m cay ak", "le ti de", "khac nx di", "ko lau ak", "ko sua ak", "soa da", "bt sua kg", "moe may", "sao dot v", "that hoc ak m", "cuoiia kakak", "lien tuc nua de", "le me ak", "son dj m", "tk cho dien", "hang le di m", "cho dien kg son ak", "ko vui r e", "k son chan the", "sua de m", "Alo", "lien tuc ma", "clmm", "tk mo coi", "dot ak m", "anh hot nhay ma", "nhanh ti", "co ti nua m", "co nua", "sap dc roi do", "co len m", "deo dc r ak", "bat luc ak",  "ga v em", "oc c loan luan", "tk cho dien", "son di m", "bat luc ak", "moi tay r ak", "duoi ak m", "ko on r ak", "k nghi ngoi ma", "speed ma m", "k speed dc ak", "oc cho z", "slow lai r ak", "sua lien tuc di", "k rot ma", "con di", "me m", "duoi ak", "le ma m", "r x", "lai victory ak", "victory ak", "victory tk slow ak", "k cay ma", "sao v", "cay ak m", "speed di", "dot ak m", "thg phe", "le lun", "oc cak", "sua dei", "kakâk", "le kg m", "tk dot", "cay r ak", "bat luc ak", "duoi r ak", "son dei", "tk ba do", "chay kg", "son le dei", "con cho", "cho dien cay", "ba m ngu", "clm rot ak", "lien tuc dei", "bo m speed", "speed ma", "kg on r ak", "oc lz ak", "tk ngu", "s duoi r", "nhay ngu ak", "nhay keo kg", "tk oc heo", "bu dai ak", "loan phim ak", "bat luc r ak", "deo laiik ak", "clm sua deii", "lienmienn akk", "chay ak", "le tay di", "suai le", "om han ak", "le m", "hap hoi ak", "thg phe", "que tay ak", "clm ga v", "le dei", "ngu ak", "kg son ak", "slow ak", "bat luc ak", "bat luc hot nhay ak", "m co hot k", "m hot j ay", "hot cut ak", "tk ga", "k speed dc", "doi hot nhay ak", "bo speed vl", "le ma may", "kg son dien a", "lej dei", "clm", "sua lofi e", "kg sua ak", "sao kg sua", "kg lien tuc ak", "rot nx ak", "sao ay nhi", "tk ga", "nhay ngu z", "sua dien loan ak", "co gang di", "co nua dei", "sao r", "bat luc ak m", "tay speed vcl", "man kg e", "man off kg m", "tk dot ngu", "oc cho ak", "cay r ak", "het son ak", "sao slow nx r", "duoi r ha", "moi tay ak", "anh uoc duoi", "anh manh vkl", "suadi em", "ot ak", "cay dien r", "kakak", "anh tay ma", "speed vl ay", "m sao lai", "m slow vc", "chat cham v", "lag ak m", "dap dt ak", "cay cmnr ak", "tk dot", "kg hoc ak", "ngu da", "sao do", "lien tuc di", "kg cham ma", "kakak", "tiep tuc de", "speed kg ays", "kg noi ak", "tk ga", "ga cay", "ot r ak", "so bo ak", "a speed vl", "keo man kg", "thg oc dai", "co nua dei", "sap dc r ay", "anh victory ak", "clm victory r", "victory r ak", "ez ak", "kaka", "lien tuc di", "sua manh", "nhanh kg", "cham ak",
"sua de", "cam a", "hang de", "s da", "sợ à m", "toc do ba", " speed dei" , "cham da ba", "phế a m", "bia a m", "sua đi m", "con ngu", "cay à ba", "m phèn ma", "choi ik m", "dg cau cuu a ba", " chậm à", "anh bá mà m", "sua de","cn mm","sao ay", "sua de","cay a","maude","nhanh de","sao doa","le de","cay a","sao ay","sua di m","cay a","djt me m","con mm","hang de em","moi tay am","duoi aak","duoi ke","clm m","cay t ak","speed m","sua de","gay a","yeu ak","met ak","phe kk","nhanh dei","ga ak","bede ak","sua de","cay ak","nhanh len","cham ak m","sao da","mau di m","sua hang kg","phe ak","sua de","nhanh de ","hang de","mau de","gay a","bede ak","dit mm","dua de","cay vl ak","sua mau de","nhanh len","nhanh kg" ,"sao da","o ke","cham da","t nhanh vvl","lien tuc dei","dua du","toc do de","sua de","le de","cay ak m","sua de m","sua chay di","con cho","ga ak cn","bia a","con cho ngu","soeed di m","dien me r","so ak","so ke","cay","chay ak","gay ke","clm m","akaka","cn mm","chill di","sua du","nhanh m","ga ak","tk cac",
]
clear()
runbanner(chontool)
delay=int(input(f'\033[1;97m[\033[1;31m</>\033[1;97m] {xanhnhat}Nhập delay(khuyến cáo trên 1s) :{vang} '))
while True:
        try:
          ping = requests.get("https://www.google.com")
          if ping.status_code == 200:
            for nd in CAU_CHUI:
                data = f"fb_dtsg={fb_dtsg}&jazoest={jazoest}&body={nd}&send=Send&tids=cid.g.{idcanspam}&wwwupp=C3&platform_xmd=&referrer=&ctype=&cver=legacy&csid=366a74a7-2d30-45dd-94c2-ad47d662dcfb"  
                response = requests.post("https://mbasic.facebook.com/messages/send/", params=params, headers=headers, data=data.encode('utf-8'))
                NOIDUNG = f"\033[1;35mĐã Gửi Thành Công\033[1;31m : \033[1;97m{nd}"
                print(f"{NOIDUNG}")
                idelay(delay)
        except Exception as e:
          print(f"{do}Lỗi bị ngắt kết lối vui lòng kết lối lại mạng để tiếp tục nhây")
          time.sleep(5)
else:
    print(f"{do}Vui lòng chọn đúng")   