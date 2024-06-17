sample_list = [1, "hello", 12.2, True]

#Accessing Elements in a List:
print(sample_list[1]) #output: hello
print(sample_list[3]) #output: True

#Lists support a variety of operations for modification, concatenation, repetition.

#Modifying 
sample_list[1] = "Ram"
print(sample_list) #output: [1, 'Ram', 12.2, True]

#Adding 
sample_list.append("Added item")
print(sample_list) #output: [1, 'Ram', 12.2, True, 'Added item']

#removing 
removed_element = sample_list.pop(0) #remove element in 0th index and give the removed element
print(sample_list) #output: ['Ram', 12.2, True, 'Added item']
print(removed_element) #output: 1

#slicing
sliced_data = sample_list[0:2] #get elements from index 0 to 2 (but exclude 2nd index)
print(sliced_data) #output: ['Ram', 12.2]


#concatenation
new_list = sample_list + ['a', 'b']
print(new_list) #output: ['Ram', 12.2, True, 'Added item', 'a', 'b']

#repetition
repete_list = sample_list * 2
print(repete_list) #output: ['Ram', 12.2, True, 'Added item', 'Ram', 12.2, True, 'Added item']       

#Slicing 
a = [12, 34, 45, 65, 23]
print(a[1:5:2]) #output: [34, 65]

b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(b[::2]) #Starts from the beginning (0), ends at the end (10), and selects every second element (1, 3, 5, 7, 9).
#output: [1, 3, 5, 7, 9]