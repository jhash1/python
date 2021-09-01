# Write a script that takes three strings from the user
# and prints the longest string together with its length.
#
# Example Input:
#     hello
#     world
#     greetings
#
# Example Output:
#     9, greetings


word1 = input("type word1:")
word2 = input("type word2:")
if len(word1) > len(word2):
    print(len(word1), word1)
else:
    print(len(word2), word2 )

##better way to print this 


