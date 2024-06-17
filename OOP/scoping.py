## Scoping
# LEGB Rule = Local Enclosed Global Built-in

def fun():
    a = 10
    print(a)

print(fun()) #output: 10
#print(a) --cannot access from outside

z = 20 #this is global 
def fun1():
    z = 60 #this is local to function fun1
    z = z + 20
    print(z)

print(fun1()) #output: 80

#we can access but cannot change directly
print(z) #output: 20


x = 50
def c():
    x = 10 # this is local to c
    #this x = 10, this is enclosed to c

    def d():
        x = 40 #this is local to d
        print("x in d() is: ", x)
        print("locals for d are: ", locals())

    print("x in c() is: ", x)
    return d()

print(c()) 
# output:
#x in c() is:  10
#x in d() is:  40
#locals for d are:  {'x': 40}

