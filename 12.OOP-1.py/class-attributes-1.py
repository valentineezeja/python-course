class User:
    active_users = 0  # added active users count

    def __init__(self, first, last, age):
        self.first = first
        self.last = last
        self.age = age
        User.active_users += 1  # increment user count after each instatiation

    # instance methods below
    def full_name(self):
        return f"{self.first} {self.last}"

    def initials(self):
        return f"{self.first[0]}.{self.last[0]}"

    def likes(self, thing):
        return f"{self.first} likes {thing}"

    def is_senior(self):
        return self.age >= 65

    def birthday(self):
        self.age += 1  # increment the age attribute of the class instance by 1
        return f"Happy {self.age}th birthday {self.first}"

    def logout(self):
        User.active_users -= 1
        return f"{self.first} has logged out. Bye"


user1 = User("Val", "Ezeja", 31)
print(user1.first, user1.last, user1.age)

# user2 = User("James", "Bloom", 40)
# print(user2.first, user2.last, user2.age)
#
# user3 = User("John", "Bosco", 55)
# print(user3.first, user2.last, user2.age)

# print(user1.full_name())
# print(user1.initials())
# print(user1.likes("moimoi"))
# print(user1.is_senior())
# print(user1.birthday())

print(User.active_users)
print(user1.logout())
print(User.active_users)