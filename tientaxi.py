# -*- coding: utf-8 -*-
"""
Created on Thu Aug 15 18:49:01 2024

@author: VanAnh
"""

print("Tinh tien taxi")
a=float(input("So km taxi di duoc la"))
if a==1:
    print("Tien taxi la 20k")
if a<=3:
    b=a*13
    print("Tien taxi la",b,"k")
if a>=4 and a<=8:
    b=3*13+ (a-3)*12
    print("Tien taxi la",b,"k")  
if a>=8:
    b=3*13+ 5*12+ (a-8)*10
    print("Tien taxi la",b,"k")
if b>100:    
    b=b*92/100
    print("Tien taxi duoc giam la",b,"k")    
    