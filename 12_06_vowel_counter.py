# Write a script that takes a string input from a user
# and prints a total count of how often each individual vowel appeared.


word = input("type a sentence with a vowel: ")
vowels = "aeiou"

for vowel in vowels:
    count = 0
    for char in word:
        if vowel == char:
            count +=1
    print(vowel, count)
    