player1 = input("Enter player1's entry ")
player2 = input("Enter player 2's entry ")

# logic here

if player1 == "rock" and player2 == "scissors":
    print("player1 wins")
elif player1 == "scissors" and player2 == "paper":
    print("player1 wins")
elif player1 == "paper" and player2 == "scissors":
    print("player2 wins")
elif player1 == "paper" and player2 == "rock":
    print("player1 wins")
elif player1 == "scissors" and player2 == "rock":
    print("player1 wins")
elif player1 == "rock" and player2 == "paper":
    print("player2 wins")
elif player1 == "rock" and player2 == "paper":
    print("player1 wins")
else:
    print("Invalid move")