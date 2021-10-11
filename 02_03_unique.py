# Write code that creates a list of all unique values in a list.
# For example:
# from typing import ItemsView


list = [1, 2, 6, 55, 2, 'hi', 4, 6, 1, 13]

unique_items = []

for item in list:
    if item not in unique_items:
        unique_items.append(item)
print(unique_items)
        



