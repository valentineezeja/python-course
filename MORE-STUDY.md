# Topics that needs further studying:

1. ## List comprehensions

*Examples:*

first = [1,2,3,4]
second = [3,4,5,6]

answer = [num for num in (first, second)]
print(answer)

numbers = range(1,101)
answer = [num for num in numbers if num % 12 == 0]
print(answer)

answer = [val for val in range(1,101) if val % 12 == 0]

word = ("amazing")
answer = [letter for letter in word if letter not in ["a","e","i","o","u"]]
print(answer)

1b. Nested list example:
nest = [[0, 1, 2], [0, 1, 2], [0, 1, 2]]
answer = [[num for num in range(0,3)] for num in range(0,3)]
print(answer)


-------------------------------------------------
2. ## Dictionary comprehensions
- Checkout the dictionaries comprehension exercise you skipped