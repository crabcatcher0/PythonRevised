sample_list = ['a', 'b', 'c', 1, 12.2, "hello"]

#length of a list
print(len(sample_list)) #output: 6

#Append an element
sample_list.append("World")
print(sample_list) #output: ['a', 'b', 'c', 1, 12.2, 'hello', 'World']

#Remove an element by value
sample_list.remove("hello")
print(sample_list) #output: ['a', 'b', 'c', 1, 12.2, 'World']

#sort elements
my_list = [1, 5, 12, 55, 23]
my_list.sort()
print(my_list) #output: [1, 5, 12, 23, 55]

#reverse 
another_list = [1, 23, 56, 7, 23]
another_list.reverse()
print(another_list) #output: [23, 7, 56, 23, 1]