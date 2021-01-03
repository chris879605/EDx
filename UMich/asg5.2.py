# -*- coding: utf-8 -*-
"""
Created on Sun Dec 27 16:58:17 2020

@author: cjames
"""

# 5.2 Write a program that repeatedly prompts a user for integer numbers 
# until the user enters 'done'. Once 'done' is entered, print out the largest
#  and smallest of the numbers. If the user enters anything other than a valid
#  number catch it with a try/except and put out an appropriate message and
#  ignore the number. Enter 7, 2, bob, 10, and 4 and match the output below.

large = None
small = None 

print('2'>'14')

while True:
    number = input("Enter Number:")
    print(number,large,small)
    if number == 'done':
        break
    try: 
        float(number)  
    except: 
        print("Invalid Response")
        continue
    number = float(number)
    if large is None:
        large = number
        small = number
        continue
    if number > large:
        print(number > large)
        large = number
    if number < small:
        small = number
    print(number,large,small)
print(large)
print(small)
    
