from random import randint  # use randint(a, b) to generate a random number between a and b

computer = randint(1,10)
user = None
while computer != user:
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
print(computer)



