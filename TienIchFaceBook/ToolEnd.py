
from random import choice, randint, shuffle
from pystyle import Add, Center, Anime, Colors, Colorate, Write, System
from os.path import isfile, isdir
from py_compile import compile
from os import listdir, mkdir, remove, rmdir, rename, chdir, name
from shutil import move, copy, rmtree
from time import sleep
from binascii import hexlify
import sys, os

    
    
strings = "abcdefghijklmnopqrstuvwxyz0123456789"  # ne pas changer svp


class Kyrie():

    def encrypt(e: str):
        e = Kyrie._ekyrie(e)
        return Kyrie._encrypt(e)

    def decrypt(e: str):
        text = Kyrie._decrypt(e)
        return Kyrie._dkyrie(text)

    def _ekyrie(text: str):

        r = ""
        for a in text:
            if a in strings:
                a = strings[strings.index(a)-1]
            r += a
        return r

    def _dkyrie(text: str):
        r = ""
        for a in text:
            if a in strings:
                i = strings.index(a)+1
                if i >= len(strings):
                    i = 0
                a = strings[i]
            r += a
        return r

    def _encrypt(text: str, key: str = None):
        if type(key) == str:
            key = sum(ord(i) for i in key)
        t = [chr(ord(t)+key)if t != "\n" else "ζ" for t in text]
        return "".join(t)

    def _decrypt(text: str, key: str = None):
        if type(key) == str:
            key = sum(ord(i) for i in key)
        return "".join(chr(ord(t)-key) if t != "ζ" else "\n" for t in text)


class Key:

    def encrypt(e: str, key: str):
        e1 = Kyrie._ekyrie(e)
        return Kyrie._encrypt(e1, key=key)

    def decrypt(e: str, key: str):
        text = Kyrie._decrypt(e, key=key)
        return Kyrie._dkyrie(text)



def ran_int(min: int = 3, max: int = 1000000):
    return randint(min, max+1)


def kramer(content: str, key: int) -> str:
    _content_ = Key.encrypt(content, key=key)
    _lines_sep_ = '/'
    
    # Join the content after encoding each line to hex
    content = _lines_sep_.join(hexlify(x.encode()).decode() for x in _content_)
    
    _names_ = ["_eval", "_exec", "_byte", "_bytes", "_bit", "_bits", "_system", "_encode", "_decode", "_delete", "_exit", "_rasputin", "_kramer"]
    _names_ = ["self." + name for name in _names_]
    shuffle(_names_)
    
    # Assign the first 12 names to globals
    global n_1, n_2, n_3, n_4, n_5, n_6, n_7, n_8, n_9, n_10, n_11, n_12
    for k in range(12):
        globals()[f'n_{k + 1}'] = _names_[k]
    
    _types_ = ("str", "float", "bool", "int")

    def _find(chars: str): 
        return "+".join(f"_n7_[{list('abcdefghijklmnopqrstuvwxyz0123456789').index(c)}]" for c in chars)

    # Define parts of the encoded structure
    _1_ = fr"""_n5_""", fr"""lambda _n9_: "".join(__import__(_n7_[1] + _n7_[8] + _n7_[13] + _n7_[0] + _n7_[18] + _n7_[2] + _n7_[8] + _n7_[8]).unhexlify(str(_n10_)).decode() for _n10_ in str(_n9_).split('{_lines_sep_}'))"""
    _2_ = fr"""_n6_""", r"""lambda _n1_: str(_n4_[_n2_](f"{_n7_[4] + _n7_[-13] + _n7_[4] + _n7_[2]}(''.join(%s), {_n7_[6] + _n7_[11] + _n7_[14] + _n7_[1] + _n7_[0] + _n7_[11] + _n7_[18]}())" % list(_n1_))).encode(_n7_[20] + _n7_[19] + _n7_[5] + _n7_[34]) if _n4_[_n2_] == eval else exit()"""
    _3_ = fr"""_n4_[_n2_]""", fr"""eval"""
    _4_ = fr"""_n1_""", fr"""lambda _n1_: exit() if _n7_[15] + _n7_[17] + _n7_[8] + _n7_[13] + _n7_[19] in open(__file__, errors=_n7_[8] + _n7_[6] + _n7_[13] + _n7_[14] + _n7_[17] + _n7_[4]).read() else "".join(_n1_ if _n1_ not in _n7_ else _n7_[_n7_.index(_n1_) + 1 if _n7_.index(_n1_) + 1 < len(_n7_) else 0] for _n1_ in "".join(chr(ord(t) - {key}) if t != "ζ" else "\n" for t in _n5_(_n1_)))"""
    _5_ = fr"""_n7_""", fr"""exit() if _n1_ else 'abcdefghijklmnopqrstuvwxyz0123456789'"""
    _6_ = fr"""_n8_""", fr"""lambda _n12_: _n6_(_n1_(_n12_))"""
    
    _all_ = [_1_, _2_, _3_, _4_, _5_, _6_]
    shuffle(_all_)
    
    _vars_content_ = ",".join(s[0] for s in _all_)
    _valors_content_ = ",".join(s[1] for s in _all_)
    
    _vars_ = _vars_content_ + "=" + _valors_content_

    # Replace placeholders in the final content
    _final_content_ = fr"""class HuongDev():
    #TácGiảHuongDev#
    def __decode__(self: object, _execute: str) -> exec:
        return (None, _n8_(_execute))[0]
    
    def __init__(self: object, _n1_: {choice(_types_)} = False, _n2_: {choice(_types_)} = 0, *_n3_: {choice(_types_)}, **_n4_: {choice(_types_)}) -> exec:
        {_vars_}
        return self.__decode__(_n4_[(_n7_[-1] + '_')[-1] + _n7_[18] + _n7_[15] + _n7_[0] + _n7_[17] + _n7_[10] + _n7_[11] + _n7_[4]])
    HuongDev(_n1_=False, _n2_=False, _sparkle='''{content}''')""".strip()

    # Remove "self." prefix for all variables where it's applied
    _final_content_ = _final_content_.replace("_n1_", n_1.lstrip("self.")).replace("_n2_", n_2.lstrip("self.")).replace("_n3_", n_3.lstrip("self.")).replace("_n4_", n_4.lstrip("self.")).replace("_n5_", n_5).replace("_n6_", n_6).replace("_n7_", n_7).replace("_n8_", n_8).replace("_n9_", n_9.lstrip("self.")).replace("_n10_", n_10.lstrip("self.")).replace("_n12_", n_12.lstrip("self."))

    return _final_content_




System.Clear()
System.Title("HuongDev")
System.Size(140, 45)

def banner():
 os.system("cls" if os.name == "nt" else "clear")
 banner = f"""
\033[1;33m██      ██╗      ████████╗ █████╗  █████╗ ██╗
\033[1;35m██╗    ╔██║      ╚══██╔══╝██╔══██╗██╔══██╗██║
\033[1;36m██║████║██║ █████╗  ██║   ██║  ██║██║  ██║██║
\033[1;37m██║    ╚██║ ╚════╝  ██║   ██║  ██║██║  ██║██║
\033[1;32m██║     ██║         ██║   ╚█████╔╝╚█████╔╝██████╗
\033[1;31m╚═╝     ╚═╝         ╚═╝    ╚════╝  ╚════╝ ╚═════╝\n
\033[1;97mTool By: \033[1;32mTrịnh Hướng            \033[1;97mPhiên Bản: \033[1;32m4.0     
\033[97m════════════════════════════════════════════════  
\033[1;97m[\033[1;91m❣\033[1;97m]\033[1;97m Tool\033[1;31m     : \033[1;97m☞ \033[1;31mTool Endcode Vip\033[1;33m♔ \033[1;97m🔫
\033[1;97m[\033[1;91m❣\033[1;97m]\033[1;97m Youtube\033[1;31m  : \033[1;97m☞ \033[1;36mHướng Dev - Kiếm Tiền Online\033[1;31m♔ \033[1;97m☜
\033[1;97m[\033[1;91m❣\033[1;97m]\033[1;97m Tik Tok\033[1;31m  : \033[1;33mhttps:\033[1;32m//www.tiktok.com\033[1;31m/m@huongdev27
\033[1;97m[\033[1;91m❣\033[1;97m]\033[1;97m Zalo\033[1;31m     : \033[1;97m☞\033[1;31m0\033[1;37m3\033[1;36m6\033[1;35m2\033[1;34m1\033[1;33m6\033[1;33m6\033[1;34m8\033[1;35m6\033[1;37m3☜
\033[1;97m[\033[1;91m❣\033[1;97m]\033[1;97m Telegram\033[1;31m : \033[1;97m☞\033[1;32mhttps://t.me/+77MuosyD-yk4MGY1🔫\033[1;97m☜
\033[97m════════════════════════════════════════════════
"""
 for X in banner:
  sys.stdout.write(X)
  sys.stdout.flush() 
  sleep(0.00125)


def main():
    System.Clear()
    banner()
    # print(Colorate.Diagonal(Colors.red_to_yellow, Center.XCenter(text)))
    _file = Write.Input("\033[❣] ✈  Nhập Tên File Pyhon cần encode -> ", Colors.red_to_yellow, interval=0.005)



    if not _file.strip() or not isfile(_file):
        Colorate.Error("Lỗi Không Tìm Thấy File!")
        return

    if '\\' in _file:
        file = _file.split('\\')[-1]
    elif '/' in _file:
        file = _file.split('/')[-1]
    else:
        file = _file

    with open(_file, 'r', encoding='utf-8', errors='ignore') as f:
        content = f.read()

    with open(file, 'w', encoding='utf-8', errors='ignore') as f:
        f.write(content)

    # print()
    # key = Write.Input("Enter your encryption key (3 - 1000000) -> ", Colors.red_to_yellow, interval=0.005)
    key = ran_int(max=1000000)

    try:
        key = int(key)
    except ValueError:
        Colorate.Error("Invalid key!")
        return

    if key < 3 or key > 1000000:
        Colorate.Error("Invalid key!")
        return


    file = file.removesuffix(".py") + "_enc.py" # hello hideaki

    content = kramer(content=content, key=key)
    with open(file, 'w', encoding='utf-8') as f:
        f.write(content)

    print('\n')

    print(Colorate.Diagonal(Colors.red_to_yellow, f"""Crypting with Kyrie Eleison...
Using key {key}...
Separating lines and spaces...
Encoding in ASCII...
Generating random variables names...
Generating two random numbers...
Creating the vars...
Shuffling the vars...
Adding the vars...
Making the final content..."""))

    print()

    compile(file)

    logsfolder = "logs"

    if isdir(logsfolder):
        rmtree(logsfolder)

    mkdir(logsfolder)

    copy(file, logsfolder)

    
    for _file in listdir("__pycache__"):
        move(f"__pycache__/{_file}", ".")
        break

    sleep(0.025)
    rmdir("__pycache__")

    if isfile(file):
        remove(file)

    copy(_file, logsfolder)

    rename(logsfolder+ '/' + _file, logsfolder+ '/' + file + 'c')

    rename(_file, file)


    print(Colorate.Diagonal(Colors.red_to_yellow, """Creating PYC file...
Moving the PYC file...
Deleting '__pycache__' folder...
Renaming PYC file..."""))

    print('\n')

    Write.Input("Thành Công Vui Lòng Enter Để Lưu File!", Colors.red_to_yellow, interval=0.005)
    return exit()

if __name__ == '__main__':
    while True:
        main()

