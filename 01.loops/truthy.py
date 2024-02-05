# Using truthy as opposed to simply printing the program helps to catch situations when a user does
# not type in something as an input for the animal name prompt
animal = input("Enter your favourite animal")
if animal:
    print (animal + " " + "is your favourite animal.")
else:
    print ("You didn't say anything")