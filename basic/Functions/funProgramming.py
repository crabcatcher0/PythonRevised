#first class citizen (treating function as variables)
#everything is object in python (functions are also object)

def fun():
    print("Hello world")

a = fun
a()
#output: Hello World