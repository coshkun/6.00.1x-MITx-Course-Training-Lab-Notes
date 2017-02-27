#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 26 05:58:22 2017

@author: coskun

This returns the fibonacci total until a given x sequence.

"""

def fib(x):
    """Assumes x an int >= 0 and
       Returns fibonacci of x"""
    if x == 0 or x == 1:
        return 1
    else:
        return fib(x-1) + fib(x-2)

for i in range(0,24):
    print(fib(i))