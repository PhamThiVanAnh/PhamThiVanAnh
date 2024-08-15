# -*- coding: utf-8 -*-
"""
Created on Thu Aug 15 14:53:43 2024

@author: VanAnh
"""

import random
chonlua = ["Keo", "Bua", "Bao"]
a = input("Chọn Keo, Bua hoặc Bao: ")
b = random.choice(chonlua)
print("Máy chọn:", b)
if a not in chonlua:
    print("Lựa chọn không hợp lệ. Vui lòng chọn Keo, Bua hoặc Bao.")
else:
    if a == b:
        print("Hòa")
    elif (a == "Keo" and b == "Bao") or (a == "Bua" and b == "Keo") or (a == "Bao" and b == "Bua"):
        print("Người chơi thắng")
    else:
        print("Người chơi thua")