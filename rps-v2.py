player1 = input("Enter player1's entry ")
player2 = input("Enter player 2's entry ")

# logic here
if player1 == player2:
    print("it's a tie")
elif player1 == "rock":
    if player2 == "paper":
        print("player1 wins")
    elif player2 == "scissors":
        print("player1 wins")
elif player1 == "scissors":
    if player2 == "paper":
        print("player1 wins")
    elif player2 == "rock":
        print("player2 wins")
elif player1 == "paper":
    if player2 == "rock":
        print("player1 wins")
    elif player2 == "scissors":
        print("player2 wins")
else:
    print("please enter a valid move")

#         and player2 == "scissors"):
#     print("player1 wins")
# elif player1 == "scissors" and player2 == "paper":
#     print("player1 wins")
# elif player1 == "paper" and player2 == "scissors":
#     print("player2 wins")
# elif player1 == "paper" and player2 == "rock":
#     print("player1 wins")
# elif player1 == "scissors" and player2 == "rock":
#     print("player1 wins")
# elif player1 == "rock" and player2 == "paper":
#     print("player2 wins")
# elif player1 == "rock" and player2 == "paper":
#     print("player1 wins")
# else:
    print("Invalid move")