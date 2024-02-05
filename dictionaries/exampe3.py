inventory = {'croissant': 19, 'bagel': 4, 'muffin': 8, 'cake': 1} #DON'T CHANGE THIS LINE!

# Make a copy of inventory and save it to a variable called stock_list USE A DICTIONARY METHOD
stock_list = inventory.copy()
print(stock_list)

a = bool(inventory == stock_list)
print(a)

b = bool(inventory is stock_list)
print(b)

# # add the value 18 to stock_list under the key "cookie"
stock_list["cake"] = 18

print(stock_list)
# remove 'cake' from stock_list USE A DICTIONARY METHOD
stock_list.pop("cake")
print(stock_list)