# -*- coding: utf-8 -*-
"""
Created on Sun Apr 26 08:45:01 2026

@author: Shreejay Divate
"""

"""
Created on Sat Apr 26
Author: Shreejay Divate
"""

class Employee:

    def _init_(self, name, salary):
        self.name = name
        self.salary = salary

    def calculate_bonus(self):
        bonus = 0.10 * self.salary
        total_salary = self.salary + bonus
        return total_salary

    def display(self):
        print("Employee Name:", self.name)
        print("Basic Salary:", self.salary)
        print("Total Salary with Bonus:", self.calculate_bonus())


# Example usage
name = input("Enter employee name: ")
salary = float(input("Enter basic salary: "))

emp = Employee(name, salary)

print("\nEmployee Details:")
emp.display()