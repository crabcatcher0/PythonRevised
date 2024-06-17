
class Human:

    population = 0     #static variables : common for all objecrs of that class
    def __init__(self, name, age):  
        self.age = age
        self.name = name

        #when a new human comes, increase the population
        Human.population += 1

    @staticmethod #this is called a decorator
        #used to modify behaviour of a function 
    def fun():
        print(Human.population)

ram = Human("Ram", 23)
data = ram.fun()
print(data)

