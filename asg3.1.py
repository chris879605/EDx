# -*- coding: utf-8 -*-
"""
Created on Sat Dec 26 18:46:44 2020

@author: cjames
"""

#Write a program to prompt the user for hours and rate per hour using
#input to compute gross pay. Pay the hourly rate for the hours up to 40
# and 1.5 times the hourly rate for all hours worked above 40 hours. Use 
#45 hours and a rate of 10.50 per hour to test the program (the pay should 
#be 498.75). You should use input to read a string and float() to convert 
#the string to a number. Do not worry about error checking the user input - 
#assume the user types numbers properly.

xh = input("Enter Hours:")
xr = input("Enter Rate:")
xh = float(xh)
xr = float(xr)
otr = xr * 1.5
if xh > 40:
    oth = xh % 40
else: oth = 0
rpay = (xh - oth) * xr
otpay = oth * otr
ttlpay = rpay + otpay
print(ttlpay)