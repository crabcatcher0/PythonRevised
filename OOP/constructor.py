# i want to assign these values, when the object is created


class Human:
    # Overriding
    def __init__(self, name, age):  #magic function and we are overriding 
        self.age = age
        self.name = name

ram = Human("Ram", 24)
gita = Human("Gita", 21)
print(ram.name) #Output: Ram
print(gita.age) #Output: 21