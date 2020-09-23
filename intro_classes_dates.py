#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

Created on Wed Sep 23 09:47:14 2020

@author: coreywade
"""

# Initialize list of numbers / (instance of the list class)
list_of_digits = [2, 7, 1, 8, 2, 8]

# Add number 2 to the list / (method of the list class)
list_of_digits.append(2)


# Create new class called person
class Person():
    
    # Initialize class with name and birthyear
    def __init__(self, name, birth_year, birth_month, birth_day_of_month):
        self.name = name
        self.birth_year = birth_year
        self.birth_month = birth_month
        self.birth_day_of_month = birth_day_of_month
    
    # Define greeting function (method)
    def greeting(self):
        return f'Hello {self.name}.'
    
    # Define function (method) that returns number of seconds on Earth
    def seconds(self):
        import datetime
        current_time = datetime.datetime.now()
        my_birthdate = datetime.datetime(self.birth_year, self.birth_month, self.birth_day_of_month, 0, 0, 0)
        current_seconds = (current_time - my_birthdate).total_seconds()
        return f'{self.name} has spent {current_seconds} seconds on Earth.'


# Create instance of Class Person
ellie = Person('Ellie', 2006, 8, 26)

# Show greeting
print(ellie.greeting())

# Show seconds on Earth
print(ellie.seconds())

lindsey = Person('Lindsey', 2006, 2, 3)
corey = Person('Corey', 1976, 4, 19)
calder = Person('Calder', 2005, 6, 3)
zorian = Person('Zorian', 2006, 11, 7)


print(calder.seconds())
print(corey.seconds())
print(zorian.seconds())
print(lindsey.seconds())




