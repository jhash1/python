# Write a script that takes a string of words and a letter from the user.
# Find the index of first occurrence of the letter in the string. For example:
#
# String input: hello world
# Letter input: o
# Result: 4

word = input("Type word here:")
letter = input("type value here:")


# returns first occurrence of Substring
result = word.find(letter)
print ("String 'letter' found at index:", result )