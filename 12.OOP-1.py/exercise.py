class BankAccount:
    def __init__(self, owner, balance=0.0):
        self.owner = owner
        self.balance = balance

    def deposit(self, num):
        self.balance += num
        return self.balance

    def withdraw(self, num):
        self.balance = self.balance - num
        return self.balance

user1 = BankAccount("Valentine")

print(user1.balance)

print(user1.deposit(4))

print(user1.withdraw(3))

print(user1.balance)