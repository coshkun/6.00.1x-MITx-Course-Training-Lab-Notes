#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 27 00:29:51 2017

@author: coskun
"""

def isPalindrome(s):
    
    def toChars(s):
        s = s.lower()
        ans=''
        for c in s:
            if c in 'abcçdefgğhıijklmnoöpqrsştuüvwxyz':
                ans = ans + c
        return ans
    
    def isPal(s):
        if len(s) <= 1:
            return True
        else:
            return s[0] == s[-1] and isPal(s[1:-1])
    
    return isPal(toChars(s))

print("")
print("Is eve a palindrome?")
print(isPalindrome("eve"))

print("")
print("Is 'Able was I, ere I saw Elba' a palindrome?")
print(isPalindrome("Able was I, ere I saw Elba"))

