# -*- coding: utf-8 -*-
"""
Created on Wed Aug 14 19:17:12 2024

@author: VanAnh
"""
a = float(input("Nhập hệ số a: "))
b = float(input("Nhập hệ số b: "))
if a == 0:
    if b == 0:
        print("Phuong trinh co vo so nghiem")
    else:
        print("Phuong trinh vo nghiem")
else:
    x = -b/a
    print("Phuong trinh co nghiem la :",x)