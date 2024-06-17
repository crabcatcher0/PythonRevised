class Human:

    population = 0     #static variables : common for all objecrs of that class
    def __init__(self, name, age):  
        self.age = age
        self.name = name

        #when a new human comes, increase the population
        Human.population += 1


ram = Human("Ram", 23)
shyam = Human("Shyam", 12)
print(ram.population)
