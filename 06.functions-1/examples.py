from random import random


def flip_coin():
    if random() < 0.5:
        return "HEAD"
    else:
        return "TAIL"


print(flip_coin())


def speak_pig():
    return "oink"


print(speak_pig())

Define a function called generate_evens
It should return a list of even numbers between 1 and 50(not including 50)


def generate_evens():
    result = []
    for num in range(1, 50):
        if num % 2 == 0:
            result.append(num)
    return result


print(generate_evens())


def yell(string):
    return f" {string.upper()}!"


print(yell("go away"))

Without adding any new lines of code, make count_dollar_signs work as intended
def count_dollar_signs(word):
    count = 0
    for char in word:
        if char == '$':
            count += 1
    return count


