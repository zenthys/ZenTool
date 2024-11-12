import sys, os, re, json, requests
from datetime import datetime
from time import sleep
import random

os.system("clear")
dau="\033[1;32m~ "
dem=0
os.system('cls' if os.name == 'nt' else 'clear')
print("\033[1;33m██      ██╗      ████████╗ █████╗  █████╗ ██╗")
print("\033[1;35m██╗    ╔██║      ╚══██╔══╝██╔══██╗██╔══██╗██║")
print("\033[1;36m██║████║██║ █████╗  ██║   ██║  ██║██║  ██║██║")
print("\033[1;37m██║    ╚██║ ╚════╝  ██║   ██║  ██║██║  ██║██║")
print("\033[1;32m██║     ██║         ██║   ╚█████╔╝╚█████╔╝██████╗")
print("\033[1;31m╚═╝     ╚═╝         ╚═╝    ╚════╝  ╚════╝ ╚═════╝\n")
print("\033[1;97mTool By: \033[1;32mTrịnh Hướng            \033[1;97mPhiên Bản: \033[1;32m4.0     ")
print("\033[97m════════════════════════════════════════════════  ")
print("\033[1;97m[\033[1;91m❣\033[1;97m]\033[1;97m Tool\033[1;31m     : \033[1;97m☞ \033[1;31mTTC - Tik Tok \033[1;33m♔ \033[1;97m🔫")
print("\033[1;97m[\033[1;91m❣\033[1;97m]\033[1;97m Youtube\033[1;31m  : \033[1;97m☞ \033[1;36mHướng Dev - Kiếm Tiền Online\033[1;31m♔ \033[1;97m☜")
print("\033[1;97m[\033[1;91m❣\033[1;97m]\033[1;97m Tik Tok\033[1;31m  : \033[1;33mhttps:\033[1;32m//www.tiktok.com\033[1;31m/m@huongdev27")
print("\033[1;97m[\033[1;91m❣\033[1;97m]\033[1;97m Zalo\033[1;31m     : \033[1;97m☞\033[1;31m0\033[1;37m3\033[1;36m6\033[1;35m2\033[1;34m1\033[1;33m6\033[1;33m6\033[1;34m8\033[1;35m6\033[1;37m3☜")
print("\033[1;97m[\033[1;91m❣\033[1;97m]\033[1;97m Telegram\033[1;31m : \033[1;97m☞\033[1;32mhttps://t.me/+77MuosyD-yk4MGY1🔫\033[1;97m☜")
print("\033[97m════════════════════════════════════════════════")
cookie=input('\033[1;97m[\033[1;91m❣\033[1;97m] \033[1;36m✈  \033[1;32mNhập Cookie TTC :\033[1;33m ')
tokenfb=input(dau+'Nhập Token Fecabook : ')
healogin={
'Host':'tuongtaccheo.com',
'user-agent':'Mozilla/5.0 (Linux; Android 9; Bee 3) AppleWebKit/537.36 (KHTML, like Gecko) coc_coc_browser/95.0.244 Mobile Chrome/89.0.4389.244 Mobile Safari/537.36',
'cookie': cookie,
}
hea={
'Host':'tuongtaccheo.com',
'user-agent':'Mozilla/5.0 (Linux; Android 9; Bee 3) AppleWebKit/537.36 (KHTML, like Gecko) coc_coc_browser/95.0.244 Mobile Chrome/89.0.4389.244 Mobile Safari/537.36',
'x-requested-with':'XMLHttpRequest',
'referer':'https://tuongtaccheo.com/kiemtien/',
'cookie': cookie,
}
heanhan={
'Host':'tuongtaccheo.com',
'user-agent':'Mozilla/5.0 (Linux; Android 9; Bee 3) AppleWebKit/537.36 (KHTML, like Gecko) coc_coc_browser/95.0.244 Mobile Chrome/89.0.4389.244 Mobile Safari/537.36',
'x-requested-with':'XMLHttpRequest',
'origin':'https://tuongtaccheo.com',
'referer':'https://tuongtaccheo.com/kiemtien/',
'cookie': cookie,
}
b= requests.get(f'https://tuongtaccheo.com/home.php', headers=healogin)
u = b.text.split('soduchinh">')[1]
xu = u.split('</strong>')[0]
print(dau+'Xu Hiện Tại: ',xu)

while (True):
 a = requests.get(f'https://tuongtaccheo.com/kiemtien/getpost.php', headers=hea)
 x = a.text.split('idpost":"')[1]
 idlike = x.split('","link')[0]
 print('🌸Đang Like ID: ',idlike) 
 urllike='https://graph.facebook.com/'+str(idlike)+'/likes'
 datalike="access_token="+tokenfb
 da={
'id':idlike,
}
 like=requests.post(urllike, data=datalike)
 nhan=json.loads(requests.post('https://tuongtaccheo.com/kiemtien/nhantien.php',headers=heanhan,data=da).text)
 print(nhan)
 sleep(10)