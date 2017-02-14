#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 14 13:51:35 2017

@author: coskun

Midterm Exam > Problem 8
20.0 points possible (graded)

Implement the fuction meet below,
f,g,and L will be supplied by system
"""
#Sample Definitions
def f(i):
    return i + 2
def g(i):
    return i > 5

L = [0, -10, 5, 6, -4]

#Problem Snippet
def applyF_filterG(L, f, g):
    """
    Assumes L is a list of integers
    Assume functions f and g are defined for you. 
    f takes in an integer, applies a function, returns another integer 
    g takes in an integer, applies a Boolean function, 
        returns either True or False
    Mutates L such that, for each element i originally in L, L contains  
        i if g(f(i)) returns True, and no other elements
    Returns the largest element in the mutated L or -1 if the list is empty
    """
    # Your code here
    mList = []
    tmp = 0
    
    #Calc New List
    for i in L:
        if g(f(i)):
            mList.append(i)
    #Apply Mutation
    L.clear()
    for i in mList:
        L.append(i)
    
    #Calc Retun Value
    if len(mList) == 0:
        return -1
    else:
        for i in mList:
            tmp = max(tmp, i)
        
    return tmp


print(applyF_filterG(L, f, g))
print(L)