# Write a program that reads in `words.txt` and prints only the words
# that have more than 20 characters (not counting whitespace).


import csv

words = []

with open("/Users/john/Downloads/python-201-main/03_file-input-output/words.txt", "r") as file:
    letter = file.readlines()
    for item in letter:
        if len(item) >= 20:
            item = item.rstrip("\n")
            words.append(item)
            
    print(words)