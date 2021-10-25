# MEMORY GAME WITH SETS
# Continuously collect number input from a user with a `while` loop.
# Confirm that the input can be converted to an integer,
# then add it to a Python `set()`.
# If the element was already in the set, noify the user that their
# input hasn't been added and deduce a point.
# If the user gets loses 5 points, quit the program.
# They wil if they manage to create a set that has more than 10 items.

points = 0
number_set = set()
while points != 5:
    number = int(input("type a number: "))
    if number in number_set:
        points += 1
        print(f"{number} already added to the list, you lost a point. You're point total is:",{points})
        if points == 5:
            print("you lost 5 points and the game is over")
            break
    elif len(number_set) == 10:
        print("You win! ")
    else:
        number_set.add(number)

    print(number_set, "number added to the list")


