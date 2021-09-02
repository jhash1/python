# Move and rename all .png files on your Desktop

# Identify all screenshots on your Desktop

# Create a new directory

# Move and rename all screenshots

from os import pardir
import pathlib

folders = pardir.__str__
pathlib.Path = '/Users/John/Desktop'
for folders in pathlib.Path:
    print(folders)