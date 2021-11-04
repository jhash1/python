# Write a script that reads in the contents of `words.txt`
# and writes the contents in reverse to a new file `words_reverse.txt`.

import csv
from os import close
from typing import ItemsView
new = []

with open("/Users/john/Downloads/python-201-main/03_file-input-output/words.txt", "r") as file:
    letter = file.readlines()
    for item in letter:
        item = item.rstrip("\n")
        item = item[::-1]
        new.append(item)


with open("/Users/john/Downloads/python-201-main/03_file-input-output/reversewords1.txt", "w") as f:
    writer = csv.writer(f)
    writer.writerows([new])