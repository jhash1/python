# Take in a number between 1 and 12 from the user
# and print the name of the associated month:
# "January", "February", ... "December"
# Print "Error" if the number from the user is not between 1 and 12.
# Use a nested `if` statement.

usermonth = input("type a number: ")
months = ( "Start", "January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December")

data = int(usermonth)


for index in range(len(months)):
    if index == data:
        print(index, months[index])
        






