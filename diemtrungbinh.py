# -*- coding: utf-8 -*-
"""
Created on Wed Aug 14 19:01:14 2024

@author: VanAnh
"""

GPA=float(input("Nhap diem trung binh (GPA): "))
if GPA < 3.5:
    print("Hoc luc kem")
elif GPA >=3.5 and GPA <=5.0:
    print("Hoc luc yeu")
elif GPA >=5.0  and GPA <=7.0:
    print("Hoc luc trung binh")
elif GPA >=7.0  and GPA <=8.0:    
    print("Hov luc kha")
elif GPA >=8.0  and GPA <=9.0:   
    print("Hoc luc gioi")
elif GPA >=9.0  and GPA <=10.0:    
    print("Hoc luc xuat sac")
    