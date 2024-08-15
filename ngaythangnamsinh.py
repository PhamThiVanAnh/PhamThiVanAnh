# -*- coding: utf-8 -*-
"""
Created on Thu Aug 15 15:07:58 2024

@author: VanAnh
"""
def la_nam_nhuan(nam):
    return (nam % 4 == 0 and nam % 100 != 0) or (nam % 400 == 0)
def so_ngay_trong_thang(thang, nam):
    if thang in [4, 6, 9, 11]:
        return 30
    elif thang == 2:
        return 29 if la_nam_nhuan(nam) else 28
    else:
        return 31
def kiem_tra_ngay_hop_le(ngay, thang, nam):
    if 1 <= thang <= 12 and 1 <= ngay <= so_ngay_trong_thang(thang, nam):
        return True
    return False
ngay = int(input("Nhập ngày: "))
thang = int(input("Nhập tháng: "))
nam = int(input("Nhập năm: "))
if kiem_tra_ngay_hop_le(ngay, thang, nam):
    print("Ngày hợp lệ")
else:
    print("Ngày không hợp lệ")