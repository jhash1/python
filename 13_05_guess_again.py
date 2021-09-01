# Re-create the guess-my-number game from scratch. Don't peek!
# This time, give your players only a certain amount of tries 
# before they lose.



import random

guess = random.randint(1,10)

count = 0

value = input("Guess a number between 1 and 10:")
while guess != value and count < 4:
    count += 1
    if guess == value:
        print("you win")
        break
    else:
        input("type a new number between 1 and 10:")

        
    