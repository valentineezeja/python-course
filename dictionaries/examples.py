# This code picks a random food item:
from random import choice #DON'T CHANGE!
food = choice(["cheese pizza", "quiche","morning bun","gummy bear","tea cake"]) #DON'T CHANGE!

#DON'T CHANGE THIS DICTIONARY EITHER!
bakery_stock = {
    "almond croissant" : 12,
    "toffee cookie": 3,
    "morning bun": 1,
    "chocolate chunk cookie": 9,
    "tea cake": 25
}

# YOUR CODE GOES BELOW:
if food in bakery_stock:
    print(f"We have {bakery_stock[food]} {food}(s) left")
else:
    print(f"The food {food} is currently not available")

-------------
method 2:
quantity = bakery_stock.get(food)
if quantity:
    print(f"{quantity} left")
else:
    print("we don't make that")
