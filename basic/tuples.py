mixed_tuple = (1, "ram", 12.2, ("nested tuple0","nested tuple1" ))
print(mixed_tuple)

#Accessing element in tuple
print(mixed_tuple[0]) #output: 1
print(mixed_tuple[3]) #output: ('nested tuple0', 'nested tuple1')

#concatenation 
tuple1 = (1, 2, 3)
tuple2 = ('a', 'b', 'c')

concatenated_tuple = tuple1 + tuple2
print(concatenated_tuple) #output: (1, 2, 3, 'a', 'b', 'c')

#Repetition
repeated_tuple = tuple1 * 3
print(repeated_tuple) #output: (1, 2, 3, 1, 2, 3, 1, 2, 3)

#counting occurance
where_tuple = (1, 2, 3, 2, 4, 4, 2)

#count occurance of value
print(where_tuple.count(2)) #output: 3
#find index of a value
print(where_tuple.index(3)) #output: 2
