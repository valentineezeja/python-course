import os

old_name = input("Enter old name:")
new_name = input("Enter old name:")


def copy(old_name, new_name):
    with open(old_name, "r") as file:
        old_content = file.read()

    with open(new_name, "w") as file:
        file.write(old_content)

    with open(new_name, "r") as file:
        new_content = file.read()

    return new_content


copied_content = copy(old_name, new_name)
print("The new contents of the file is:")
print(copied_content)
