# -*- Check whether year is leap year or not*-
"""
Created on Fri Mar 13 06:59:29 2026

@author: Shreejay Divate
"""

year = int(input("Enter year: "))
if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
    print("Leap Year")
else:
    print("Not a Leap Year")
