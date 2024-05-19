# List

my_list = [1,2,3,4]

# you can access list elements using indexing
my_list[2] #output : 3, because the list starts with index 0
my_list[-1] #output: 4, if negative, then the list will start from the last index

# List can be nested
list_nested = [[1,2,3],[4,5,6],[7,8,9]]

# List are mutable  
# you can insert, delete element in the list

list_nested.append([10,11,12])  
# will add new list at the end
print(list_nested)