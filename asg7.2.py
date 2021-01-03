# -*- coding: utf-8 -*-
"""
Created on Fri Jan  1 16:07:31 2021

@author: cjames
"""

# 7.2 Write a program that prompts for a file name, then opens that file and 
# reads through the file, looking for lines of the form:
# X-DSPAM-Confidence:    0.8475
# Count these lines and extract the floating point values from each of the 
# lines and compute the average of those values and produce an output as shown
#  below. Do not use the sum() function or a variable named sum in your solution.
# You can download the sample data at http://www.py4e.com/code3/mbox-short.txt
#  when you are testing below enter mbox-short.txt as the file name.

fname = input("Enter file name: ")
fpath = 'C:/Users/cjames/Downloads/'
fpathname = fpath + fname
data = open(fpathname)
x=0
xtotal = 0
for line in data:
    line = line.rstrip()
    if line.startswith('X-DSPAM-Confidence:'):
        # print(line)
        x=x+1
        xtotal = xtotal + float(line[21:])
#         print(line[21:])
# print('Count',x)
# print('Sum',xtotal)
print('Average spam confidence:',xtotal/x)
# stringform = data.read()
# print(stringform.upper())