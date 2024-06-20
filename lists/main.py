# lists
#a = [i for i in range(1, 11)]
#print(a)

#Accessing Elements of a single-dimensioned list
#negative indexing
#accessing elements of multi-dimensioned list

#A list containing multiples of 5 up to 20

#
#my_list = [i*5 for i in range(1, 5)]
#print(my_list)


### negative indexing
#accessing elements from the last
#A list containing multiples of 5 up to 20.
#when we don't know the length of the list 
#my_list = [5, 10, 15, 20]
#print(my_list[-1])

##multi-dimensional list
#example
my_list2 = [[1, 2, 3], "Neso", [4, 5, 6]]
a = len(my_list2[0])
indexes_of_0 = a - 1
print(indexes_of_0)

#how to access the value 'b' in the above list?
my_list3 = [1, 2, 3, ['a', 'b', 'c'], 5, 6]
b = my_list3[3][1]
print(b)