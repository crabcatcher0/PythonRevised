class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

#self parameter is a reference to the current instance of the class, 
# and is used to access variables that belongs to the class.
    def myfunc(self):
        return f"Hello ! {self.name}. I am {self.age} years old."


data = Person("Ram", 23)
#del data.name ## delete the name 
print(data.myfunc())