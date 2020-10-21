#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct  6 19:25:24 2020

@author: coreywade
"""


#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 30 10:13:01 2020

@author: coreywade

This document creates a Fractions class that will be used to perform 
basic operations on fractions that return fractions
"""

# Create Fraction
class Frac():
    
    # Initialize class with numerator and denominator
    def __init__(self, num, den):
        self.num = num
        self.den = den
    
    # This is what you get with print() (display fraction)
    def __str__(self):
        return f'{self.num}/{self.den}'
    
    # This is what you get with + (adding two fractions)
    def __add__(self, frac2):
        new_num = self.num * frac2.den + frac2.num * self.den
        new_den = self.den * frac2.den
        new_frac = Frac(new_num, new_den)
        return new_frac
# 1/2 + 1/3 =  3/6 + 2/6
# n1/d1 + n2/d2 = (n1d2 + n2d1)/d1d2
        
class Mixed_Frac(Frac):
    def __init__(self, whole, num, den):
        self.whole = whole
        self.num = num
        self.den = den
    
    def __str__(self):
        return f'{self.whole} {self.num}/{self.den}'
    
    def improper(self):
        new_num = self.den * self.whole + self.num
        new_den = self.den
        return Frac(new_num, new_den)
    
print(Mixed_Frac(3, 1, 2))
print(Mixed_Frac(3, 1, 2).improper())

m1 = Mixed_Frac(3, 1, 2)
m2 = Mixed_Frac(3, 1, 3)
print(m1 + m2)               