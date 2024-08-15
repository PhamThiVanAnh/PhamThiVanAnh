# -*- coding: utf-8 -*-
"""
Created on Wed Aug 14 20:02:23 2024

@author: Student
"""

import math
a = float(input("Nhập hệ số a: "))
b = float(input("Nhập hệ số b: "))
c = float(input("Nhập hệ số c: "))
delta = b**2 - 4*a*c
if delta < 0:
  print ("Phuong trinh vo nghiem")
elif delta == 0:
    print ("Phuong trinh co nghiem kep: x = {x}")
else:
    print ("Phuong trinh vo nghiem")
if delta > 0:
    x1 = (-b + math.sqrt(delta))/ (2*a)
    x2 = (-b - math.sqrt(delta))/ (2*a)
    print ("Phuong trinh co hai nghiem phan biet: x1 = {x1}, x2 = {x2}")