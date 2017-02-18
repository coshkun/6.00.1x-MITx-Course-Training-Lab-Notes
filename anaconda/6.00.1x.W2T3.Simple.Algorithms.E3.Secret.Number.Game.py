#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 18 02:46:54 2017

@author: coskun

6.00.1x.W2T3.Simple.Algorithms.E3.Secret.Number.Game

Your Secret Number Game :)

The program works as follows: you (the user) thinks of an integer 
between 0 (inclusive) and 100 (not inclusive). The computer makes guesses, 
and you give it input - is its guess too high or too low? 
Using bisection search, the computer will guess the user's secret number!
"""

# Paste your code into this box
x = 99
low=0
height=x

g=(low+height)/2  #change this with  )//2 to pass the exam

print("Please think of a number between 0 and 100!")

while True:
    print("Is your secret number "+str(round(g))+"?")  #change this with str(g)
    inp = input("(Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly.): ")
    if (inp == str("l")) or (inp == str("h")) or (inp == str("c")):
        pass
    else:
        print("Sorry, I did not understand your input.")
        continue
    
    if inp == str("l"):
        low = g
    elif inp == str("h"):
        height = g
    elif inp == str("c"):
        break
    
    g = (low + height)/2
    
print("Game over. Your secret number was: ",str(round(g))) #change this with str(g)