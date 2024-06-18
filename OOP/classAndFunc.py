# which rectangle has a larger area.

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self): #The __str__() controls what should be returned when the class object is represented as a string.
        return f"{self.name}({self.age})"

data = Person("John", 12)
print(data)