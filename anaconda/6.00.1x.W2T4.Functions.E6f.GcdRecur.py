#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 26 20:34:48 2017

@author: coskun

Exercise: gcd recur
5.0 points possible (graded)
ESTIMATED TIME TO COMPLETE: 6 minutes

The greatest common divisor of two positive integers is the largest integer 
that divides each of them without remainder. For example,

gcd(2, 12) = 2
gcd(6, 12) = 6
gcd(9, 12) = 3
gcd(17, 12) = 1

A clever mathematical trick (due to Euclid) makes it easy to find greatest 
common divisors. Suppose that a and b are two positive integers:

If b = 0, then the answer is a

Otherwise, gcd(a, b) is the same as gcd(b, a % b)

See this website for an example of Euclid's algorithm being used to find 
the gcd.(https://en.wikipedia.org/wiki/Euclidean_algorithm#Worked_example)

Write a function gcdRecur(a, b) that implements this idea recursively. 
This function takes in two positive integers and returns one integer.

"""

def gcdRecur(a, b):
    '''
    a, b: positive integers
    
    returns: a positive integer, the greatest common divisor of a & b.
    '''
    # Your code here
    #rslt = 1
    if a > b:
        return gcdRecur(a-b, b)
    elif b > a:
        return gcdRecur(a, b-a)
    else:
        return a
    

print(gcdRecur(8,12))