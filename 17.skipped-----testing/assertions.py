def eat_junk(food):
    assert food in [
        "rice",
        "beans", "akara",
        "okpa"
    ],  "Food must be in the list"
    return f"your chosen food is {food}"


print(eat_junk("rice"))
