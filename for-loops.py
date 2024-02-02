Simple for loop
num = 0
num = input("how many times do I tell you ")
num = int(num)
for times in range(num):
    print(f"clean your room {num} times")


#a bit advanced
num = range(1,21)
for number in num:
    if number == 13 or number == 4:
        print(f"{number} is UNLUCKY")
    elif number % 2 == 0:
        print(f"{number} is even")
    else:
        print(f"{number} is odd")

#optional approach
num = range(1,21)
for number in num:
    if number == 13 or number == 4:
        state = "UNLUCKY"
    elif number % 2 == 0:
        state = "even"
    else:
        state = "odd"