#Note that the following methods are instance methods, not class metods yet
class User:
    def __init__(self, first, last, age):
        self.first = first
        self.last = last
        self.age = age

    def full_name(self):
        return f"{self.first} {self.last}"

    def initials(self):
        return f"{self.first[0]}.{self.last[0]}"

    def likes(self, thing):
        return f"{self.first} likes {thing}"

    def is_senior(self):
        return self.age >= 65

    def birthday(self):
        self.age +=1 #increment the age attribute of the class instance by 1
        return f"Happy {self.age}th birthday {self.first}"



user1 = User("Val", "Ez", 31)
print(user1.first, user1.last, user1.age)

# user2 = User("James", "Bloom", 40)
# print(user2.first, user2.last, user2.age)
#
# user3 = User("John", "Bosco", 55)
# print(user3.first, user2.last, user2.age)

print(user1.full_name())
print(user1.initials())
print(user1.likes("moimoi"))
print(user1.is_senior())
print(user1.birthday())