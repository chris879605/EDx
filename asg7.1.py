# -*- coding: utf-8 -*-
"""
Created on Fri Jan  1 15:09:34 2021

@author: cjames
"""

# 7.1 Write a program that prompts for a file name, then opens that file and 
# reads through the file, and print the contents of the file in upper case. 
# Use the file words.txt to produce the output below.
# You can download the sample data at http://www.py4e.com/code3/words.txt

fname = input("Enter file name: ")
fpath = 'C:/Users/cjames/Documents/'
fpathname = fpath + fname
data = open(fpathname)
# for line in data:
#     print(line.rstrip())
stringform = data.read()
print(stringform.upper())