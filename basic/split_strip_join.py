# split, strip and join


#strip
#removes extra space
a = "  2 3 4 5 6  "
print(a.strip()) #output: 2 3 4 5 6


#split
#breaks the string according to space and creats a list
b = "2 4 5 6"
li = b.split(" ")
print(li) #output: ['2', '4', '5', '6']

#apply the int function to every element of the list
li = list(map(int, li))
print(li) #output: [2, 4, 5, 6]
print(sum(li)) #output: 17

#input into list

user = input("Enter a number: ")
print("This is a number: " + user)

user = user.split(" ")
print(user)

li = list(map(int, user))
print(li)

#output: 
#Enter a number: 1 2 3 4
#This is a number: 1 2 3 4
#['1', '2', '3', '4']
#[1, 2, 3, 4]

