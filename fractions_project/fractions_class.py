#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct  7 10:27:39 2020

@author: coreywade
"""

class Fraction():
    
    # Initialize class with numerator and denominator
    def __init__(self, num, den):
        self.num = int(num)
        self.den = int(den)
        try:
            self.num = int(num)
            self.den = int(den)
            assert self.den != 0, "Denom can't be zero"
        except:
            print("Inputs must be integers. Try again.")
        #except:
        #    raise TypeError("Inputs must be integers")
        
        #assert type(self.num) or type(self.den) == int, "Inputs must be integers"
    
    # This is what you get with print() (display fraction)
    def GCD(self, a, b):
        if a == 0:
            return b
        if b == 0:
            return a
        return self.GCD(b, a%b)
    
# call GCD to maintain self    
    def gcd(self):
        return self.GCD(self.num, self.den)

    def reduce(self):
        divisor = self.gcd()
        new_num = int(self.num / divisor)
        new_den = int(self.den / divisor)
        new_frac = Fraction(new_num, new_den)
        return new_frac 

    def __str__(self):
        self = self.reduce()
        if self.den == 1:
            return f'{self.num}'
        elif self.num == 0:
            return f'{self.num}'
        else:
            return f'{self.num}/{self.den}'

    
    # This is what you get with + (adding two fractions)
    def __add__(self, frac2):
        new_num = self.num * frac2.den + frac2.num * self.den
        new_den = self.den * frac2.den
        new_frac = Fraction(new_num, new_den)
        new_frac = new_frac.reduce()
        return new_frac  

            
    # SAME WITHOUT THE FRACTIONS CLASS

    # Add Subtraction, multiplication, and division
    
# Create new subclass Improper that inherits all properties from Fraction
class Mixed(Fraction):
    
    def __init__(self, whole, num, den):
        self.whole = whole
        self.num = num
        self.den = den
    
    def __str__(self):
        return f'{self.whole} {self.num}/{self.den}'

    def improper(self):
        new_num = self.den * self.whole + self.num
        new_den = self.den
        return Fraction(new_num, new_den)

    
    def __add__(self, frac2):
        return self.improper() + frac2.improper()
    
print('''This is a fractions class in progress. You can initialize a 
      fraction as follows:
          
        1. Initialize fractions:
            one_half = Fraction(1, 2)
              
        2. Add fractions:
            one_half + one_half
        
        3. Display fractions:
            print(one_half)
          
          ''')
        