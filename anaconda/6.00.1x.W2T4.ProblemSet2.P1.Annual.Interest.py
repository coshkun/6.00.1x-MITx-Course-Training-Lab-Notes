#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar  4 23:30:51 2017

@author: coskun

Problem 1 - Paying Debt off in a Year
10.0 points possible (graded)

Write a program to calculate the credit card balance after 
one year if a person only pays the minimum monthly payment 
required by the credit card company each month.

The following variables contain values as described below:

balance - the outstanding balance on the credit card
annualInterestRate - annual interest rate as a decimal
monthlyPaymentRate - minimum monthly payment rate as a decimal

For each month, calculate statements on the monthly payment and 
remaining balance. At the end of 12 months, print out the remaining balance. 
Be sure to print out no more than two decimal digits of accuracy - so print

print("Remaining balance: 813.41")

"""

#test Case 1:
balance = 42
annualInterestRate = 0.2
monthlyPaymentRate = 0.04
grndTotal = 0

#Test Case 2:
balance = 484
annualInterestRate = 0.2
monthlyPaymentRate = 0.04

def unpaidBalance(Balance, MonthlyPaymentRate):
    return Balance - (Balance * MonthlyPaymentRate)

def updatedNextMount(Unpaid, AnnualInterestRate):
    return Unpaid + ((AnnualInterestRate/12.0) * Unpaid)

def annualSubDebt(balance, annualInterestRate, monthlyPaymentRate, mount = 12):
    """ This Recursive Function calculates mountly interest applied debt and,
        returns grand total debit.
    """
    #b1 = updatedNextMount(unpaidBalance(balance, monthlyPaymentRate), annualInterestRate)
    
    if mount == 0:
        print("Month",12 - mount,"Remaining balance:",balance)
        return balance
    
    print("Month",12 - mount,"Remaining balance:",balance)
    mount = mount - 1
    ub = unpaidBalance(balance, monthlyPaymentRate)
    return annualSubDebt(updatedNextMount(ub, annualInterestRate), annualInterestRate, monthlyPaymentRate, mount)

grndTotal = round(annualSubDebt(balance, annualInterestRate, monthlyPaymentRate), 2)
print("Remaining balance:",grndTotal)