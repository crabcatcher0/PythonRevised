#Handling Duplicate Keys:

my_dict = {
    "name": "Ram",
    "age": 12,
    "school": "TJMC",
    "age": 14 #updates the value according to key
}

print(my_dict)

#output
#{'name': 'Ram', 'age': 14, 'school': 'TJMC'}