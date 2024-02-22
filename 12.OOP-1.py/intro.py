# class User:
#     pass
#
#
# user1 = User()
# print(user1)
# print(type(user1))
# print(type(User))

class User:
    def __init__(self, first, last, age):
        self.first = first
        self.last = last
        self.age = age


user1 = User("Val", "Ez", 31)
print(user1.first, user1.last, user1.age)

user2 = User("James", "Bloom", 40)
print(user2.first, user2.last, user2.age)

user3 = User("John", "Bosco", 55)
print(user3.first, user2.last, user2.age)