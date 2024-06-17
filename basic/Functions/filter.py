
## example: I only want even numbers
# in this, the function return True or False only.

a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def isEven(x): #check is a num is even or not
    if x % 2 == 0: # if the remainder is 0
        return True
    else:
        return False

data = list(filter(isEven, a))
print(data) #output: [2, 4, 6, 8, 10]

#using lambda function

lam_data = list(filter(lambda x: x % 2 == 0, a))
print(lam_data) #output: [2, 4, 6, 8, 10]