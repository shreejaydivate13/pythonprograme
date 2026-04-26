# -*- coding: utf-8 -*-
"""
Created on Sun Apr 26 08:39:26 2026

@author: Shreeejay Divate
"""

# -- coding: utf-8 --
"""
Created on Sat Apr 26
Author: Shreejay Divate
"""

class BankAccount:

    def _init_(self, name, balance):
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        self.balance = self.balance + amount
        print("Amount Deposited:", amount)

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance = self.balance - amount
            print("Amount Withdrawn:", amount)
        else:
            print("Insufficient Balance")

    def display(self):
        print("Account Holder Name:", self.name)
        print("Current Balance:", self.balance)


# Example usage
name = input("Enter account holder name: ")
balance = float(input("Enter initial balance: "))

acc = BankAccount(name, balance)

deposit_amount = float(input("Enter deposit amount: "))
acc.deposit(deposit_amount)

withdraw_amount = float(input("Enter withdraw amount: "))
acc.withdraw(withdraw_amount)

print("\nAccount Details:")
acc.display()