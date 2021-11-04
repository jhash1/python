# Refactor your file counter script to use `pathlib` also for
# reading and writing to your CSV file. Make sure to handle the
# path in a way so that you can run the script from anywhere.


import csv
import pathlib 

count = {"": 8, ".csv": 2, ".md": 2, ".png": 11}

csvfile = pathlib.Path(r'/Users/john/Downloads/python-201-main/03_file-input-output/testitem.txt')
countwriter = csv.writer(csvfile)
data = [count[""], count[".csv"], count[".md"], count[".png"]]
countwriter.writerow(data)