# Convert some sequences you got to know into other sequences:
# - Convert the string shown below into a tuple.
# - Convert the tuple into a list.
# - Change the `c` character in your list into a `k`
# - Convert the list back into a tuple.

string = "codingnomads"

new_tup = tuple(string)

new_list = list(new_tup)
for i in range(len(new_list)):
      if new_list[i] == 'c':
        new_list[i] = 'k'
print(new_list)