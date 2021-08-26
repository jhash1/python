# Take in the following three values from the user:
# 1. investment amount
# 2. interest rate in percentage
# 3. number of years to invest
#
# Calculate the future values and print them to the console.

amount = input("Type in a value: ")
interestrate = int(input("Type in a rate: "))
rate = amount * interestrate
years = input("How many years do you want to invest: ")

print(int(years) * int(rate) * int(amount))

