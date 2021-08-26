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
    print(word1, len(word1))
else:
    print(word2, len(word2))


