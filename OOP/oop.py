# simplest class

class Human:
    age = 0
    name = "Ram"

human_obj = Human() 
human2_obj = Human()
human_obj.age = 21
ind = human2_obj.age


# whenever we create an object, a constructor is called automatically
# constructor is a function

print(human_obj.name,human2_obj.age) #output: Ram 0
print(human_obj.age) #output: 0
print(human_obj.name) #output: Ram
print (ind) #output: 21