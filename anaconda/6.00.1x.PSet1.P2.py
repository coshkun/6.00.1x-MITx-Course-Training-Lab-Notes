# -*- coding: utf-8 -*-
"""
Created on Sun Feb 12 13:12:43 2017

Problemset1 - Problem 2
Note:
    's' is given by system like s = 'azcbobobegghakl'
@author: coskun
"""
s = 'azcbobobegghakl'
# Paste your code into this box 
nvl=0
ask=''
for c in s:
    if len(ask) < 3:
        ask += c
    elif len(ask) == 3:
        ask = ask[1:len(ask)]
        ask += c

    if ask=='bob':
        nvl += 1
        
print("Number of times bob occurs is: " + str(nvl))