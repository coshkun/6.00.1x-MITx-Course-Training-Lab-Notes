# -*- coding: utf-8 -*-
"""
Created on Sun Feb 12 13:12:43 2017

Problemset1 - Problem 3
Note:
    's' is given by system like s = 'azcbobobegghakl'
@author: coskun
"""
s = 'azcbobobegghaklabcbcd'
# Paste your code into this box 
rslt = ''
tmp = ''
n = len(s)
while n > 0:
    c = s[len(s)-n]
    #print(c)
    n -= 1
    
    for i in range(0, n-1):
        nxt = s[len(s)-n]
        if c < nxt:
            tmp += c
            break
        else:
            if len(tmp) > len(rslt):
                rslt = tmp
            tmp = ''
            break
    #print("tmp: " + tmp)
#print("rslt: " + rslt)
print("Longest substring in alphabetical order is: " + rslt)
