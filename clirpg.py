# Build a CLI RPG game following the instructions from the course.
# Ask the player for their name.
# Display a message that greets them and introduces them to the game world.
# Present them with a choice between two doors.
# If they choose the left door, they'll see an empty room.
# If they choose the right door, then they encounter a dragon.
# In both cases, they have the option to return to the previous room or interact further.
# When in the seemingly empty room, they can choose to look around. If they do so, they will find a sword. They can choose to take it or leave it.
# When encountering the dragon, they have the choice to fight it.
# If they have the sword from the other room, then they will be able to defeat it and win the game.
# If they don't have the sword, then they will be eaten by the dragon and lose the game.

playername = input("Type in your name: ")

print(f"Welcome to the game {playername}")

Choice = input("Please choose a path, left or right: ")

if Choice == "right":
    print("You encountered a Dragon!")

if Choice == "left":
    print("The room is empty! ")
Explore = input("Do you want to look around: ")

if Explore == "yes":
   print("take a look around: ")

Sword = input("Did you find a sword: ")
Dragon = input("Do you want to fight the dragon: ")
if Sword == "yes" and Dragon == "yes":
    print("You won the fight!")
elif Sword == "no" and Dragon == "yes": 
    print("You lost the fight and the dragon ate you ALIVE!")
elif Sword == "yes" and  Dragon == "no":
    print("You will walk away and not fight the dragon!")
else:
    print(f"{playername}, you entered the room with the dragon and a sword")




