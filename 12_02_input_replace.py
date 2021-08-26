# Write a script that takes a string of words and a symbol from the user.
# Replace all occurrences of the first letter with the symbol. For example:
#
# String input: more python programming please
# Symbol input: §
# Result: §ore python progra§§ing please



symbol = input("write a symbol: ")
words = input("type something: ")


for i in range(words):
    for x in (words):
        if x == "aeiou":