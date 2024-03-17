import os
cwd = os.getcwd()

with open("testfile.txt") as file:
    content = file.read()

print(cwd)
print(f"content of the file you seek is: /n {content}")
