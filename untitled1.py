#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 14 10:21:30 2020

@author: coreywade
"""


#Factorial(n) = n * (n - 1) * (n - 2) * ... * 2 * 1

#Factorial(3) = 3 * 2 * 1

# Fact(3) = 3!

# Fact(3) = 3 * Fact(2)


def fact(n):
    n = abs(n)
    if n == 1:
        return 1
    else:
        return n * fact(n-1)

print(fact(4))

print(fact(-1))