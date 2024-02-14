# def numbers_add(*args):
#     total = 0
#     for num in args:
#         total += num
#     return total
#
#
# print(numbers_add(2, 3, 4))

def greeting(*args):
    if "val" in args and "love" in args:
        return "you are welcome home"
    return "sorry, I don't know you"


print(greeting("hello", "coolio", "dayum"))
print(greeting("goom", "great!", "val", "love"))
