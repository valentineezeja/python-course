class Chicken:
    total_eggs = 0

    def __init__(self, name, species, egg=0):
        self.name = name
        self.species = species
        self.egg = egg

    def lay_egg(self):
        self.egg += 1
        Chicken.total_eggs += 1
        return self.egg


user1 = Chicken("okuko", "hen")
user2 = Chicken("fowl", "rooster")

my_egg = user1.lay_egg()
my_egg2 = user2.lay_egg()

print(my_egg)
print(my_egg2)
print(Chicken.total_eggs)
