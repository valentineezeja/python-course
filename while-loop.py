simple while
num = 1
while num <=10:
    print(num)
    num += 1 #this is the same as doing num = num+1

#a bit advanced
emoji = "😀"
for num in range(1,11):
    print (emoji * num)

solving using while loop
emoji = "😀"
num = 1
while num <=10:
    print(emoji * num)
    num += 1

# input repetition example
text = input("enter your message here \n")
while text != "stop copying me":
    print(text)
    text = input("enter your message here \n")
print("OKAY YOU WIN")


from random import randint  # use randint(a, b) to generate a random number between a and b

number = 0 # store random number in here, each time through
i = 0  # i should be incremented by one each iteration
number = randint(1,10)
while number != 5:
    i += 1
    number = randint(1, 10)
