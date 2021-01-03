# -*- coding: utf-8 -*-
"""
Created on Sun Dec 27 20:47:12 2020

@author: cjames
"""

# 6.5 Write code using find() and string slicing (see section 6.10) 
# to extract the number at the end of the line below. Convert the extracted 
# value to a floating point number and print it out.

text = "X-DSPAM-Confidence:    0.8475";
pos = text.find('.')
answer = text[pos:]
answer = float(answer)
print(answer)
