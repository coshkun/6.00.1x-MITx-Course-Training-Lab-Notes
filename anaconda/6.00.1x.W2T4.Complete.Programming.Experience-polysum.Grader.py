#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 28 02:31:04 2017

@author: coskun

Complete Programming Experience: polysum > Grader
10.0 points possible (ungraded)

A regular polygon has n number of sides. Each side has length s.

The area of a regular polygon is: 0.25∗n∗s2 / (tan(π/n))

The perimeter of a polygon is: length of the boundary of the polygon

Write a function called polysum that takes 2 arguments, n and s. 
This function should sum the area and square of the perimeter of the 
regular polygon. The function returns the sum, rounded to 4 decimal places.
"""

def polysum(n, s):
    """
    " This function should sum the area and square of the perimeter of 
    " the regular polygon. The function returns the sum, 
    " rounded to 4 decimal places.
    "
    " n is the positive int >= 3 which is the num of edges
    " s is the lenght of one edge.
    """
    #Safety Belt
    if n < 3 or s < 1:
        return 0
    #My Code Here :)
    import math
    area = (0.25*n*(s**2)) / (math.tan(math.pi/n))
    perimeter = n*s
    return round(area + (perimeter**2), 4)
    
print(polysum(23, 1))