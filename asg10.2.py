# -*- coding: utf-8 -*-
"""
Created on Sat Jan  2 17:52:55 2021

@author: cjames
"""

# 10.2 Write a program to read through the mbox-short.txt and figure out 
# the distribution by hour of the day for each of the messages. You can 
# pull the hour out from the 'From ' line by finding the time and then 
# splitting the string a second time using a colon.
# From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
# Once you have accumulated the counts for each hour, print out the counts, 
# sorted by hour as shown below.

fname = input("Enter file name: ")
fpath = 'C:/Users/cjames/Downloads/'
if len(fname) < 1 : fname = "mbox-short.txt"
handle = open(fpath + fname)
# print(handle.read())
hrcount = dict()
for line in handle:
    line = line.rstrip()
    if line.startswith('From '):
        # print(line)
        chunks = line.split()
        # print(chunks[5])
        hour = chunks[5].split(':')
        # print(hour[1])
        hrcount[hour[0]] = hrcount.get(hour[0], 0) + 1
# print(hrcount) 
# print(hrcount)
hrcountsorted = sorted(hrcount.items())
print(hrcountsorted)
for x in hrcountsorted:
    print(x[0],x[1])
# print(hrcount.items())
# print(hrcount)
# for k,v in hrcount.items():
#     tmptup = (v,k)
#     tmp.append(tmptup)
# tmp = sorted(tmp, reverse = True)
# # print(tmp)
# for v,k in tmp:
    # print(k,v)
# hrcount = list()
# for k,v in tmp.items():
#     tmptup = (v,k)
#     hrcount.append(tmptup)



        
    