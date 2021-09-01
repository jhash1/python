# Create a sarcastic program that asks a user for their honest opinion,
# then prints the same sentence back to them in aLtErNaTiNg CaPs.


program = input("type in a word: ")

result = ''
index = 0

for char in program:
    if index % 2 == 0:
        result += char.upper()
    else:
        result += char.lower()
    index +=1
print(result)