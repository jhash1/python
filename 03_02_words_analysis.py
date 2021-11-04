# Read in all the words from the `words.txt` file.
# Then find and print:

# 1. The shortest word (if there is a tie, print all)
# 2. The longest word (if there is a tie, print all)
# 3. The total number of words in the file.

import csv
new_list = []
a = 0
number_list = []
small = []
large = []

with open("/Users/john/Downloads/python-201-main/03_file-input-output/words.txt", "r") as file:
    # letter = file.readlines()
    new_list.extend(file)
    for word in new_list:
        a = len(word)
        number_list.append(a)
    x = min(number_list)
    y = max(number_list)
for char in new_list:
    if len(char) == x:
        char= char[:-1]
        small.append(char)
    if len(char) == y:
        char= char[:-1]
        large.append(char)
print(f"Smallest words are {small}")
print(f"Largest words are {large}")
print(f"Length of the list is {len(new_list)}")



        
        
        
