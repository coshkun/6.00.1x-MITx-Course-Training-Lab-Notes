# -*- coding: utf-8 -*-
"""
Created on Mon Feb 13 23:01:20 2017

@author: coskun
"""

#Sample inputs
d1 = {1:30, 2:20, 3:30, 5:80}
d2 = {1:40, 2:50, 3:60, 4:70, 6:90}

def f(a,b):
    return a+b

def dict_interdiff(d1, d2):
    '''
    d1, d2: dicts whose keys and values are integers
    Returns a tuple of dictionaries according to the instructions above
    '''
    # Your code here
    myTpl = ({},{})
    intersect = myTpl[0]
    difference= myTpl[1]
    
    if len(d1) == len(d2):
        #--Equality
        print(len(d1))
    elif len(d1) < len(d2):
        #--Get intersect based d1
        for i in d1.keys():
            if i in d2:
                intersect[i] = f(d1[i],d2[i])
            else:
                difference[i] = d1[i]
        #--Get dif based d2
        for i in d2.keys():
            if i not in d1:
                difference[i] = d2[i]
    else:
        #--Get intersect and dif based d2
        print(len(d2))
    
    print(list(myTpl))
    
dict_interdiff(d1, d2)
#print(d1.keys())