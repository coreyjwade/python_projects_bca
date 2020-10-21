#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 14 09:49:19 2020

@author: coreywade
"""


def fact(n):
    if n == 1:
        return 1
    else:
        return n * fact(n-1)
    
#print(fact(4))

def fib(n):
    if n == 1 or n == 0:
        return 1
    else: 
        return fib(n-1) + fib(n-2)

#print(fib(5))

def gcd(a, b):
    #if b > a:
     #   c = a
      #  a = b
       # b = c
    if b == 0:
        return a
    else:
        return gcd(b, a%b)

print(gcd(8, 12))

def add(n):
    if n == 1:
        return 1
    else :
        return n + add(n-1)

print(add(10))