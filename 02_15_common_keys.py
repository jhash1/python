# Write a script that takes the following two dictionaries
# and creates a new dictionary by combining the common keys
# and adding the values of duplicate keys together.
# Use `for` loops to iterate over these dictionaries
# to accomplish this task.
#
# Example output:
# result = {"a": 3, "b": 2, "c": 7 , "d": 2}

dict1 = {"a": 1, "b": 2, "c": 3}
dict2 = {"a": 2, "c": 4 , "d": 2}

dict3 = {**dict1, **dict2}
for key, value in dict3.items():
    if key in dict1 and key in dict2:
        dict3[key] = dict2[key] + dict1[key]

print(dict3)