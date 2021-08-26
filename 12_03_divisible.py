# Write a program that takes a number between 1 and 1,000,000,000
# from the user and determines whether it is divisible by 3 using an `if` statement.
# Print the result.


program = int(input("Pick a number between 1 and 1,000,000,000: "))
if  program % 3 == 0:
    print("yes")
else: 
    print("nope")

