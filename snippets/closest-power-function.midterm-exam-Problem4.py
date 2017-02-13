# -*- coding: utf-8 -*-
"""
Created on Mon Feb 13 16:43:18 2017

@author: coskun
"""

def closest_power(base, num):
    '''
    base: base of the exponential, integer > 1
    num: number you want to be closest to, integer > 0
    Find the integer exponent such that base**exponent is closest to num.
    Note that the base**exponent may be either greater or smaller than num.
    In case of a tie, return the smaller value.
    Returns the exponent.
    '''
    exp = 0
    # Limitations here
    if base <= 1:
        return 0
    if num <= 0:
        return 0
    if base == num:
        return 1
    if num == 1:
        return 0
    if abs(base) > abs(num):
        return 0
    else:
        i = 1
        tmp = 0
        while abs(base)**i < abs(num):
            tmp = i
            i += 1
        if abs(num) == abs(base)**i:
            #global exp
            exp = i
        elif (abs(num) - abs(base)**tmp) == (abs(base)**i - abs(num)):
            # in case of tie :)
            exp = tmp
        elif (abs(num) - abs(base)**tmp) < (abs(base)**i - abs(num)):
            #global exp
            exp = tmp
        else:
            #global exp
            exp = i
    #Return Conditions
    return exp

print(closest_power(3,210))