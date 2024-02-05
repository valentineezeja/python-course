original = [1, 2, 3, 4]
new_list = [num / 2 for num in original]
print(new_list)

--------------

Using list comprehensions:

answer = [name[0] for name in ["Elie", "Tim", "Matt"]] #prints out first letters
answer2 = [val for val in [1,2,3,4,5,6] if val % 2 == 0] #prints out even numbers
Using good old manual loops:

answer = []
for person in ["Elie", "Tim", "Matt"]:
    answer.append(person[0])
answer2 = []
for num in [1,2,3,4,5,6]:
    if num % 2 == 0:
        answer2.append(num)