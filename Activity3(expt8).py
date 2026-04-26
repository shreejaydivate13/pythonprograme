# -*- coding: utf-8 -*-
"""
Created on Sun Apr 26 10:23:46 2026

@author: Shreejay Divate
"""
# Bill splitting program with zero-check

try:
    total_bill = float(input("Enter total bill amount: "))
    people = int(input("Enter number of people: "))

    if people <= 0:
        print("Invalid input! Number of people must be greater than zero.")
    else:
        share = total_bill / people
        print("Each person should pay:", share)

except ValueError:
    print("Invalid input! Please enter numbers only.")
