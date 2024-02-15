# def my_func(**kwargs):
#     val =""
#     if kwargs.get('val') == 'special':
#         return "Good boy"
#     return "Not today"
#
#
# print(my_func(val="special"))


# def my_colour(**kwargs):
#     for person, colour in kwargs.items():
#         print(f"{person}'s favourite colour is {colour}")
#     return "no colour specified"
#
# print(my_colour(obi="red", juke="black", ada="green"))

# def my_new_func(**kwargs):
#     if "valentine" in kwargs and kwargs["valentine"] == "good":
#         return "You're a good boy"
#     elif "valentine" in kwargs:
#         return f"{kwargs['valentine']} Valentine!!"
#     return "Sorry, I don't know you"
#
#
# print(my_new_func(David = "hello"))
# print(my_new_func(valentine= "good"))
# print(my_new_func(valentine= "bad"))

# Exercise...
# Define combine_words below:
def combine_words(word, **kwargs):
    if "prefix" in kwargs:
        return f"{kwargs['prefix']}{word}"  # you can also use return here without f"
    elif "suffix" in kwargs:
        print(f"{word}{kwargs['suffix']}")  # you can also use return here without f"
    else:
        return word


print(combine_words(word="child", prefix="man"))
print(combine_words(word="child", suffix="boo"))
print(combine_words(good="doo", tree="loo"))
