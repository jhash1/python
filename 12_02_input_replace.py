# Write a script that takes a string of words and a symbol from the user.
# Replace all occurrences of the first letter with the symbol. For example:
#
# String input: more python programming please
# Symbol input: §
# Result: §ore python progra§§ing please


symbol = '$'
words = 'hello world'

vowels = 'aeiou'

for char in words:
    for vowel in vowels:
        if char == vowel:
            char = symbol
    print(char, end='')
