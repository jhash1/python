# Re-create the guess-my-number game from scratch. Don't peek!
# This time, give your players only a certain amount of tries 
# before they lose.



import random

guess = random.randint(1,10)

count = 0

value = input("Guess a number between 1 and 10:")
    while guess != value:
count += 1
        print("you win")


# use a number generator to create random num between x and y
# create an input to ask user to guess a number
# create counter to start at 0 and increment to 4
# print "you lose if number is not guessed and tries hit 4"

        
