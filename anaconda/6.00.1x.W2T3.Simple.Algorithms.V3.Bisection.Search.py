#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 17 19:56:15 2017

@author: coskun

6.00.1x.W2T3.Simple.Algorithms.V3.Bisection.Search
EXAMPLE OF SQUARE ROOT
"""

x = 25
epsilon = 0.01
numGuess = 0
low = 0.0
height = x

g = (height + low)/2.0

while abs(g**2 - x) >= epsilon:
    print('low= '+str(low)+' height= '+str(height)+' guess= '+str(g))
    numGuess += 1
    
    if g**2 > x:
        height = g
    else:
        low = g
    
    g = (height + low)/2.0 #make a new guess
print("Number of Guess is " + str(numGuess))
print(str(g), "is close enoght to square root of ", str(x))