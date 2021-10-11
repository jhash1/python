# Take in 10 numbers from the user. Place the numbers in a list.
# You can also use the provided random `randlist` list
# to simulate user input.
# Find the largest number in the list and print the result.
# Calculate the product of all of the numbers in the list.

count = 0
number_list = []

while count <= 2:
    number = input('type in a number: ')
    number = int(number)
    number_list.append(number)
    count += 1


number_list.sort()
print(number_list[-1])

sum = sum(number_list)
print(sum)

