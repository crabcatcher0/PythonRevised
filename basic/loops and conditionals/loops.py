# for loops 


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

for num in range(1, 5): #5 is excluded
    print(num)

#output
#1
#2
#3
#4

z = [i for i in range(1, 6)]
print(z)
#output: [1, 2, 3, 4, 5]


#using index to iterate in for loops
bob = [12, 34, 2]

for index, i in enumerate(bob):
    print(index, i)

#output: 
#0 12
#1 34
#2 2

t = [2*i for i in range(1, 11)]
print(t)
#output: [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]


number = list(range(1, 11))

for g in number:
    if g == 6:
        break
        #continue
    print(g, end=" ")
    #output break: 1 2 3 4 5
    #output continue: 1 2 3 4 5 7 8 9 10 