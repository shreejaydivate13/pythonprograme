# -*- Find the factorial of a number using loops.-*-
"""
Created on Fri Mar 13 07:09:11 2026

@author: Shreejay Divate
"""
n = int(input("Enter number:"))
fact = 1
for i in range(1, n + 1):
    fact = fact * i
print("Factorial:", fact)
