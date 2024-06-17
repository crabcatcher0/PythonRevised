class Parent:
    f = 80
    def __init__(self, value):
        self.value = value

class Child(Parent):
    def __init__(self, value, name):
        super().__init__(value)
        self.name = name

obj = Child(67, "RAM")
data = obj.f, obj.value, obj.name
print(data) #output: (80, 67, 'RAM')



