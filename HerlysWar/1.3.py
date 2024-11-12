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
\033[1;33m║\033[1;34m▶ Nhóm Zalo  : \033[1;35mhttps://zalo.me/g/azfjwi735     \033[1;33m║
\033[1;33m║\033[1;34m▶ FaceBook : \033[1;35mhttps://bom.so/tZxIW6             \033[1;33m║
\033[1;33m║\033[1;34m▶ Zalo : \033[1;35mhttps://bom.so/wnhs5C                 \033[1;33m║
\033[1;33m║\033[1;34m▶ Mua Key Vip Cứ Liên Hệ Zalo Nhé              \033[1;33m║
\033[1;33m╚═══════════════════════════════════════════════╝
\033[1;32m-------------------------------------------------"""
clear()
runbanner(chontool)
idcanspam=input(f'{trang}[{do}</>{trang}] \033[1;32m\033[1mID Box Cần Réo Tên :{vang} ')
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
chon_name = str(input(f"{vang}Điền Tên Cần Réo {trang}: "))
if chon_name.lower() == "{chon_name}":
      lag = "{chon_name}"
elif chon_name.lower() == "ndjjdkd":
      lag = " "
else:
      CAU_CHUI = [
f"sua di {chon_name}",
f"co len con {chon_name}",
f"son hang len em {chon_name}",
f"sao m yeu v {chon_name} ",
f"co ti nua {chon_name}",
f"sao kia cham a {chon_name}",
f"hang hai len ti chu {chon_name}",
f"toi sang di {chon_name}",
f"co gang ti con cho {chon_name}",
f"yeu v con {chon_name}",
f"con cho {chon_name} co de",
f"sao m cam kia {chon_name}",
f"ga v {chon_name}",
f"may so a k dam chat hang ak {chon_name}",
f"m ga ma {chon_name}",
f"may ngu ro ma {chon_name}",
f"con {chon_name} an hai ma",
f"cai cun ak {chon_name}",
f"may con gi khac ko vay {chon_name}",
f"hoc dot nen nhay dot ak {chon_name}",
f"co ti di em {chon_name}",
f"meu a {chon_name}",
f"sao meu kia {chon_name}",
f"tao da cho m meu dau {chon_name}",
f"va le di con {chon_name} dot",
f"sao kia {chon_name}",
f"tu bo r a {chon_name}",
f"manh me ti di con {chon_name}",
f"co len con cho {chon_name} ngu",
f"😆 cay tao a con di {chon_name}",
f"so tao a {chon_name}",
f"sao cham roi kia {chon_name}",
f"cay lam phai kh {chon_name}",
f"{chon_name} ot anh cmnr",
f"may con choi a {chon_name}",
f"lam ti keo de {chon_name}",
f"moi do da met r ha {chon_name}",
f"sao ga ma son v {chon_name}",
f"son nhu luc dau cho tao di con {chon_name} dot",
f"sao duoi roi kia {chon_name}",
f"ai cho m nhai vay {chon_name}",
f"cay lam r a {chon_name}",
f"tu bo di em {chon_name}",
f"may nghi may lam t cay dc ha {chon_name}",
f"m dang cay ma {chon_name}",
f"tao dang hanh m ma {chon_name}",
f"keo nhay kg ay {chon_name}",
f"con mo coi {chon_name}",
f"co len {chon_name} oc cho",
f"hang tiep di {chon_name}",
f"toi sang k em {chon_name}",
f"met roi ha {chon_name}",
f"speed ti dc ko {chon_name}",
f"m ga ma {chon_name}",
f"thay phien a {chon_name}",
f"tui anh thay phien ban vo loz me con {chon_name} ma kaka",
f"so tao a con cho {chon_name}",
f"anh win me roi {chon_name} dot",
f"ga ma hay the hien ha {chon_name}",
f"con mo coi {chon_name} keo cai ko em",
f"co len de {chon_name}",
f"sao moi 1 ti ma da cam roi {chon_name}",
f"yeu vay ak {chon_name}",
f"sao kia {chon_name}",
f"bat luc r ak {chon_name}",
f"tim cach roi ha {chon_name}",
f"ai cuu dc m a :)) {chon_name}",
f"anh ba cmnr ma {chon_name}",
f"sao m ga vay {chon_name}",
f"hang le cho tao di {chon_name}",
f"con mo coi {chon_name}",
f"on k em {chon_name}",
f"bat on roi a {chon_name}",
f"may oc a con cho {chon_name}",
f"me may ngu a {chon_name}",
f"bu cac cha m k em {chon_name}",
f"mo coi {chon_name} cay anh ha",
f"me m dot tu roi a {chon_name}",
f"phe vay {chon_name}",
f"m on k {chon_name}",
f"mo coi kia {chon_name}",
f"sao v so r a {chon_name}",
f"co gang ti em {chon_name}",
f"cay cu lam r ha {chon_name}",
f"dien dai di em {chon_name}",
f"chay nuoc dai bo r a em {chon_name}",
f"sao kia dung so anh ma {chon_name}",
f"may run a:)) {chon_name}",
f"thg {chon_name} mo coi",
f"cay tao lam ha {chon_name}",
f"lgbt len phim ngu ak em {chon_name}",
f"thg cac giet cha mang me {chon_name}",
f"sua manh eii {chon_name}",
f"may chet r a:)) {chon_name}",
f"sao chet kia {chon_name}",
f"bi t hanh nen muon chet a {chon_name}",
f"con {chon_name} loz ngu kaka",
f"sao kia {chon_name}",
f"manh len kia {chon_name}",
f"yeu sinh ly a {chon_name}",
f"sua de {chon_name}",
f"cay a {chon_name}",
f"hang de {chon_name}",
f"con ga {chon_name}",
f"phe vat {chon_name}",
f"oc cho {chon_name}",
f"me m bi t du hap hoi kia con {chon_name}",
f"on ko em {chon_name}",
f"bat on ak {chon_name}",
f"o kiaaa sao vayy {chon_name}",
f"hang hai de {chon_name}",
f"chay ak {chon_name}",
f"so ak {chon_name}",
f"quiu luon roi ak {chon_name}",
f"may dot ak {chon_name}",
f"cac ngu {chon_name}",
f"chay de {chon_name}",
f"chat hang len {chon_name}",
f"co len {chon_name}",
f"{chon_name} mo coi",
f"cn cho ngu {chon_name}",
f"oc cac {chon_name}",
f"di du {chon_name}",
f"du kia {chon_name}",
f"cun v {chon_name}",
f"r luon con {chon_name} bi ngu roi",
f"met r am {chon_name}",
f"kkakak",
f"sao du {chon_name}",
f"cac con {chon_name}",
f"ngu kia {chon_name}",
f"chat manh de {chon_name}",
f"hang ee {chon_name}",
f"clm thk oc cho {chon_name}",
f"sua chay de {chon_name}",
f"sua manh eei {chon_name}",
f"may oc a con {chon_name}",
f"tao cho m chay a {chon_name}",
f"con mo coi {chon_name}",
f"may chay a con di lon {chon_name}",
f"sua de {chon_name}",
f"con phen {chon_name}",
f"bat on ho {chon_name}",
f"s do  {chon_name}",
f"sua lien tuc de {chon_name}",
f"moi tay ak {chon_name}",
f"choi t giet cha ma m ne {chon_name}",
f"hang xiu de {chon_name}",
f"th ngu {chon_name}",
f"len daica bieu ne {chon_name}",
f"sua chill de {chon_name}",
f"m thich du ko da {chon_name}",
f"son hang dc kg {chon_name}",
f"cam chay nhen {chon_name}",
f"m mau de {chon_name}",
f"duoi ak {chon_name}",
f"th ngu {chon_name}",
f"con {chon_name} len day anh sut chet me may",
f"m khoc ak {chon_name}",
f"sua lien tuc de {chon_name}",
f"thg {chon_name} cho dien",
f"bi ngu ak {chon_name}",
f"speed de {chon_name}",
f"cham v cn culi {chon_name}",
f"hoang loan ak {chon_name}",
f"bat on ak {chon_name}",
f"run ak {chon_name}",
f"chay ak {chon_name}",
f"duoi ak {chon_name}",
f"met r ak {chon_name}",
f"sua mau {chon_name}",
f"manh dan len {chon_name}",
f"nhanh t cho co hoi cuu ma m ne {chon_name}",
f"cam mach me nha {chon_name}",
f"ao war ak {chon_name}",
f"tk {chon_name} dot v ak",
f"cham chap ak {chon_name}",
f"th cho bua m sao v {chon_name}",
f"th dau buoi mat cho {chon_name}",
f"cam hoang loan ma {chon_name}",
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