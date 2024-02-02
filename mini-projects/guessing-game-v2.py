#with the option to keep playing the game after winning
from random import randint  # use randint(a, b) to generate a random number between a and b

computer = randint(1,10)
user = None
while True:                             #Note that this also works with computer != user
    computer = randint(1, 10)
    user = int(input("Enter your guess "))
    print(f"computer's guess: {computer}")
    print(f"user's guess: {user}")
    if computer > user:
        print("too low, go up a bit")
    elif computer < user:
        print("too high, go lower")
    else:
        print("You WON!!")
        ctd_play = input("Do you want to continue playing? Y/N ")
        if ctd_play == "Y":
            computer = randint(1, 5)
            user = None
        else:
            print("Thank you for playing")
            break

