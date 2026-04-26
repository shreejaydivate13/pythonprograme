# -*- coding: utf-8 -*-
"""
Created on Sun Apr 26 10:20:05 2026

@author: Shreejay Divate
"""
# Registration form with age validation

try:
    name = input("Enter your name: ")

    age = int(input("Enter your age: "))

    if age <= 0:
        print("Invalid age! Age must be greater than 0.")
    elif age < 18:
        print("You are underage. Registration not allowed.")
    else:
        print("Registration successful!")
        print("Name:", name)
        print("Age:", age)

except ValueError:
    print("Invalid input! Please enter a valid number for age.")
