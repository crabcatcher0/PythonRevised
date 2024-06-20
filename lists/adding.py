#adding elements in a list
#append()
#insert()
#extend()

#append() method add item at the end of the list

#syntax : list.append(vale) where value is a value we want to add in list

user_list1 = (input("Enter a list: ")).split(', ')
user_list2 = (input("Enter another list: ")).split(', ')
merged = user_list1 + user_list2

sorted_list = sorted(merged)
print(sorted_list)


