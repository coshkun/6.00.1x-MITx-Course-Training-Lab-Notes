#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 19 03:16:17 2017

@author: coskun
"""

x = float(input("Enter a decimal number between 0 and 1: "))

p = 0
while ((2**p)*x)%1 != 0:
    print("Reminder: " + str((2**p)*x - int((2**p)*x)) + " while p= "+str(p))
    p += 1
    
num = int((2**p)*x)
#print(num)
result = ''
if num == 0:
    result = '0'
while num > 0:
    result = str(num%2) + result
    num = num//2
#now we have the binary representation

for i in range(p - len(result)):
    result = '0' + result

result = result[0:-p] + '.' + result[-p:]
print("Binary representetion of "+str(x)+' is '+ result)
