# -*- coding: utf-8 -*-
"""
Created on Wed Aug 14 20:09:17 2024

@author: Student
"""

import math
a = float(input("Nhập hệ số a: "))
b = float(input("Nhập hệ số b: "))
c = float(input("Nhập hệ số c: "))
if a + b + c and b + c > a:
    print("a, b , c la ba canh cua mot tam giac.")
    if a == b == c:
        print("Tam giac deu.")
    elif (math.isclose(a**2 + b**2, c**2) or
          math.isclose(a**2 + c**2, b**2) or
          math.isclose(b**2 + c**2, a**2)):
        print("Tam giac vuong.")
    elif a == b == c:
        print("Tam giac can.")
    else:
        print("Tam giac thuong.")
else:
    print("a , b, c khong phai la ba canh cua mot tam giac.")        