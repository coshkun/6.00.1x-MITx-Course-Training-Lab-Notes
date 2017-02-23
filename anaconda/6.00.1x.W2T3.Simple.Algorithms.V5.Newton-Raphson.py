#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 22 17:23:58 2017

Newton-Raphson Algorithm

this sample tries to find the root of a fraction
using a better guessing method offered by Newton and Raphson.
the main idea is to make a new gues with using it's first derivative.

such as;

   new g => g - f(g)/f'(g)

@author: coskun
"""

epsilon = 0.01
y = 24.0
guess = y/2.0
numGuess = 0

while abs((guess*guess) - y) > epsilon:
    numGuess += 1
    guess = guess - (((guess**2) - y)/(2*guess))

print("Number of attempts is ", numGuess)
print("Square root of "+str(y)+" is "+str(guess))