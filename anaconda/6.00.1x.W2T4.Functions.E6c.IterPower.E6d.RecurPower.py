#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 24 00:51:39 2017

@author: coskun
"""

def is_even(i):
    """
    " Input: i, as a positive integer.
    " Returns True if i is even.
    """
    return i%2 == 0


def recurPower(base, exp):
    '''
    base: int or float.
    exp: int >= 0
 
    returns: int or float, base^exp
    '''
    # Your code here
    if exp == 0:
        return 1
    else:
        return base * recurPower(base, exp - 1)

def iterPower(base, exp):
    '''
    base: int or float.
    exp: int >= 0
 
    returns: int or float, base^exp
    '''
    # Your code here
    prod = 1
    while exp >= 1:
        prod *= base
        exp -= 1
    return prod