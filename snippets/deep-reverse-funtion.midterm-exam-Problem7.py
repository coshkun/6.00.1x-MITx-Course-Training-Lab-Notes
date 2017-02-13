# -*- coding: utf-8 -*-
"""
Created on Mon Feb 13 19:04:45 2017

@author: coskun

Midterm Exam > Problem 6
15.0 points possible (graded)

Implement a function that meets the specifications below.

For example, if L = [[1, 2], [3, 4], [5, 6, 7]] 
then deep_reverse(L) mutates L to be [[7, 6, 5], [4, 3], [2, 1]]

"""
#Sample Hand Input
L = [[1, 2], [3, 4], [5, 6, 7]]

def deep_reverse_copy(L):
    """ assumes L is a list of lists whose elements are ints
    Mutates L such that it reverses its elements and also 
    reverses the order of the int elements in every element of L. 
    It does not return anything.
    """
    # Your code here
    R = L[::-1]
    mSize = len(L)
    for i in range(mSize):
        R[i] = R[i][::-1]
    return R

def deep_reverse(L):  # This will be the correct answer for test case
    """ assumes L is a list of lists whose elements are ints
    Mutates L such that it reverses its elements and also 
    reverses the order of the int elements in every element of L. 
    It does not return anything.
    """
    # Your code here
    L.reverse()
    mSize = len(L)
    for i in range(mSize):
        L[i] = L[i][::-1]

print(L)
deep_reverse(L)
print(L)