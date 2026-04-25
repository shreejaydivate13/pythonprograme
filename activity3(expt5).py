# -*- coding: utf-8 -*-
"""
Created on Sat Apr 25 12:20:23 2026

@author: Shreejay Divate
"""

# Initial shop inventory dictionary
inventory = {
    "apples": 50,
    "bananas": 20,
    "oranges": 15
}

def add_stock(item, quantity):
    """Adds quantity to an existing item or creates a new entry."""
    if item in inventory:
        inventory[item] += quantity
    else:
        inventory[item] = quantity
    print(f"Updated {item}: {inventory[item]} in stock.")

# Example: Adding new stock
add_stock("apples", 10)  # Updates existing
add_stock("mangoes", 5)  # Adds new item

print("\nFinal Inventory:", inventory)