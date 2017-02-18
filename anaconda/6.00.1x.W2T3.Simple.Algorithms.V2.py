#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 14 14:53:31 2017

@author: coskun
"""

cube = 29
epsilon = 0.01
guess = 0.0
increment = 0.001
num_guesses = 0

while abs(guess**3 -cube) >= epsilon and guess <= cube:
    guess += increment
    num_guesses += 1
print("number of guess= ", num_guesses)
if abs(guess**3 - cube) >= epsilon:
    print("failed on cube root of", cube)
else:
    print(guess, "is close enoght to cube root of", cube)
