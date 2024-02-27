class Human:
    def __init__(self, first, last, age):
        self.first = first
        self.last = last
        if age >=0:
            self._age = age # internal use _
        else:
            self._age = 0 # internal use _

    @property  #getter
    def age(self):
        return self._age

    @age.setter   #setter
    def age(self, value):
        if value >= 0:
            self._age = value # internal use _
        else:
            raise ValueError("age can't be negative")

jane = Human("Jane", "Goodall", -9)
print(jane.age)
jane.age = 20
print(jane.age)