import random    #you can use from random import radint; that way you only need to use radint(....) for your main command
# player1 = input("Enter player1's entry ")
player2 = input("Enter player 2's entry ").lower()
auto = random.randint(1,3)
if auto == 1:
    computer = "rock"
elif auto == 2:
    computer = "paper"
elif auto == 3:
    computer = "scissors"
print(f"computer played {computer}")

if computer == player2:
    print("it's a tie")
elif computer == "rock":
    if player2 == "paper":
        print("player2 wins")
    elif player2 == "scissors":
        print("computer wins")
elif computer == "scissors":
    if player2 == "paper":
        print("computer wins")
    elif player2 == "rock":
        print("player2 wins")
elif computer == "paper":
    if player2 == "rock":
        print("computer wins")
    elif player2 == "scissors":
        print("player2 wins")
else:
    print("please enter a valid move")