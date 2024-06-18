#closure

def outer_func():
        message = "hi"

        def inner_fun():
            print("These are the locals: ", locals())
            print(message) #free variables

        return inner_fun

my_func = outer_func()
print(my_func()) #output: hi ,These are the locals:  {'message': 'hi'}
