# -*- coding: utf-8 -*-
"""
Created on Sat Apr 25 11:47:14 2026

@author: Shreejay Divate
"""
# Taking input for the first set
set1 = set(map(int, input("Enter elements of first set (space-separated): ").split()))

# Taking input for the second set
set2 = set(map(int, input("Enter elements of second set (space-separated): ").split()))

# Union of two sets
union_set = set1 | set2        # or set1.union(set2)

# Intersection of two sets
intersection_set = set1 & set2   # or set1.intersection(set2)

# Display the results
print("Union of the sets:", union_set)
print("Intersection of the sets:", intersection_set)
