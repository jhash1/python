# Write a script that takes a text input from the user
# and creates a dictionary that maps the letters in the string
# to the number of times they occur. For example:
#
# user_input = "hello"
# result = {"h": 1, "e": 1, "l": 2, "o": 1}



# text = input("type a word:" )
# dict = {}
# for char in text:
#     if char in dict:
#         dict[char] += 1
#     else:
#         dict[char] = 1
# print(dict)

punc = ['!','?','.']

text = input("type a word: ")
dict ={"UPPER_CASE":0, "LOWER_CASE":0, "PUNCTUATIONS" :0, "TOTALCHAR":0}
for char in text:
    if char.islower():
        dict["LOWER_CASE"]+=1
    elif char.isupper():
            dict["UPPER_CASE"]+=1
    elif char in punc:
        dict["PUNCTUATIONS"]+=1
        print(char)
    elif char.isalpha():
        dict["TOTALCHAR"]+=1
    
# {"TOTALCHAR"} = {'LOWER_CASE'} + {'UPPER_CASE'}
    

print(dict)
    
# Write a script that takes a sentence from the user and returns:

# the number of lower case letters
# the number of uppercase letters
# the number of punctuations characters
# the total number of characters
# Use a dictionary to store the count of each of the above.    
