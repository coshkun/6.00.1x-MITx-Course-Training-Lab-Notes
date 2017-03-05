#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar  5 02:26:49 2017

@author: coskun

Problem 2
1/1 point (ungraded)

Now write a program that calculates the minimum fixed monthly payment 
needed in order pay off a credit card balance within 12 months. 
By a fixed monthly payment, we mean a single number which does not 
change each month, but instead is a constant amount that will be 
paid each month.

result should be like this:

    "Lowest Payment: 180"

Assume that the interest is compounded monthly according to the balance 
at the end of the month (after the payment for that month is made). 
The monthly payment must be a multiple of $10 and is the same for all months. 
Notice that it is possible for the balance to become negative 
using this payment scheme, which is okay.
"""

#Test Case 1:
balance = 3329
annualInterestRate = 0.2

def unpaidBalance(Balance, FixedPayment):
    return Balance - FixedPayment

def updatedNextMount(Unpaid, AnnualInterestRate):
    return Unpaid + ((AnnualInterestRate/12.0) * Unpaid)

def annualSubDebt(balance, annualInterestRate, fixedPaymentRate, mount = 12):
    """ This Recursive Function calculates mountly interest applied debt and,
        returns grand total debit.
    """
    #b1 = updatedNextMount(unpaidBalance(balance, monthlyPaymentRate), annualInterestRate)
    
    if mount == 0:
        #print("Month",12 - mount,"Remaining balance:",balance)
        return balance
    
    #print("Month",12 - mount,"Remaining balance:",balance)
    mount = mount - 1
    ub = unpaidBalance(balance, fixedPaymentRate)
    return annualSubDebt(updatedNextMount(ub, annualInterestRate), annualInterestRate, fixedPaymentRate, mount)

def minDebtPayingAmount(balance, annualInterestRate):
    """ This calculates the minimum monthly payment who can close all debit
        with total annual interests.
    """
    i = 0
    rslt = 1
    while rslt > 0:
        i += 10
        rslt = annualSubDebt(balance, annualInterestRate, i)
    print("Lowest Payment:",i)

minDebtPayingAmount(balance, annualInterestRate)
