# -*- coding: utf-8 -*-
"""
Created on Fri Jan  1 17:56:33 2021

@author: cjames
"""

# 8.4 Open the file romeo.txt and read it line by line. 
# For each line, split the line into a list of words using the split() method. 
# The program should build a list of words. For each word on each line check 
# to see if the word is already in the list and if not append it to the list. 
# When the program completes, sort and print the resulting words in 
# alphabetical order.

fname = input("Enter file name: ")
fpath = 'C:/Users/cjames/Downloads/'
fpathname = fpath + fname
data = open(fpathname)
wordlist = list()
for line in data:
    words = line.split()
    print(words)
    for x in words:
        print(x)
        print(x in wordlist)
        test = x in wordlist
        if test is False:
            wordlist.append(x)
        else: 
            print('WordAlreadyExists')   
wordlist.sort()
print(wordlist)        
