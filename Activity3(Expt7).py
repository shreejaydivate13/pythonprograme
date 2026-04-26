# -*- coding: utf-8 -*-
"""
Created on Sun Apr 26 08:52:39 2026

@author: Shreejay Divate
"""
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 26
Author: Shreejay Divate
"""

class Student:

    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def calculate_grade(self):
        if self.marks >= 75:
            return "A"
        elif self.marks >= 60:
            return "B"
        elif self.marks >= 40:
            return "C"
        else:
            return "Fail"

    def display(self):
        print("Student Name:", self.name)
        print("Marks:", self.marks)
        print("Grade:", self.calculate_grade())


# Example usage
name = input("Enter student name: ")
marks = float(input("Enter marks: "))

stu = Student(name, marks)

print("\nStudent Details:")
stu.display()
