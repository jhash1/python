# Re-create the guess-my-number game from scratch. Don't peek!
# This time, give your players only a certain amount of tries 
# before they lose.



number = 6
number = int(number)

count = 0

while True:
    guess = input("Pick one num between 1 and 10: ")
    if count == 3:
        print("out of guesses")
        break
    guess = int(guess)
    if number != guess:
        count += 1
        print("keep going")
    elif number == guess:
        print("you got it")
        break
   




# use a number generator to create random num between x and y
# create an input to ask user to guess a number
# create counter to start at 0 and increment to 4
# print "you lose if number is not guessed and tries hit 4"

        
