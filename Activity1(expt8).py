# -*- coding: utf-8 -*-
"""
Created on Sun Apr 26 10:16:27 2026

@author: Shreejay Divate
"""
class BankAccount:
    def __init__(self, balance):
        self.balance = balance

    def withdraw(self, amount):
        if amount <= 0:
            print("Invalid amount. Please enter a positive value.")
        elif amount > self.balance:
            print("Insufficient balance!")
        else:
            self.balance -= amount
            print("Withdrawal successful.")
            print("Remaining balance:", self.balance)


# Main program
try:
    balance = float(input("Enter your account balance: "))
    account = BankAccount(balance)

    amount = float(input("Enter amount to withdraw: "))
    account.withdraw(amount)

except ValueError:
    print("Invalid input! Please enter numbers only.")
