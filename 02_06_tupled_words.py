# Write a script that takes a string from the user
# and creates a list that contains a tuple for each word.
# For example:


# result_list = [('h', 'e', 'l', 'l', 'o'), ('w', 'o', 'r', 'l', 'd')]

word = "hello world"
word.split(',')
tup = tuple(word)

new_list = list(tup)

hello = tup[0:5]
world = tup[6:11]

result_list = []

result_list.append(hello)
result_list.append(world)
print(result_list)