#loops 
#for and while loops

a = [4, 5, 6]

for num in a:
    print(num)
#output: 
#4
#5
#6

name = 'RAM'
for char in name:
    print(char)
#output:
#R
#A
#m

for num in range(1, 5):
    print(num)

#output
#1
#2
#3
#4

#using index to iterate in for loops
bob = [12, 34, 2]

for index, i in enumerate(bob):
    print(index, i)

#output: 
#0 12
#1 34
#2 2