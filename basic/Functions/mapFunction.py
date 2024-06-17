#it applies a given function to each element of iterable

# multiply each number in list by 2

a = [1, 2, 3, 4, 5]

def multipl(x): # x here is each element of a, not whole a
    return 2 * x

final = list(map(multipl, a))

print(final) #output: [2, 4, 6, 8, 10]

# converting into lambda function

lam_fun = list(map(lambda x:2 * x, a))
print(lam_fun)  #output: [2, 4, 6, 8, 10]

#make every element power 2 of that element
b = [1, 2, 3, 4, 5]
power_data = list(map(lambda x: x ** 2, a))
print(power_data) #output: [1, 4, 9, 16, 25]
