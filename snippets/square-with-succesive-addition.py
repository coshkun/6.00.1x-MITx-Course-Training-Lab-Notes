# -*- coding: utf-8 -*-
"""
Spyder Editor
Successive Addition method as n^2 = n + n + n ... (n pieces)

This is a temporary script file.
"""
def Square(x):
    return SquareHelper(abs(x), abs(x))

def SquareHelper(n, x):
    if n == 0:
        return 0
    return SquareHelper(n-1, x) + x

print(Square(4))
