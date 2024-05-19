# Tuple
# Similar to lists but immutable (cannot be changed once created)

my_tuple = ("arin","kannazuki","kanao","yuzuki")

# indexing
my_tuple[0] # output: arin
my_tuple[-1] # output: yuzuki

# slicing
print(my_tuple[1:3])  #output: ('kannazuki','kanao')
print(my_tuple[:2])  #output: ('arin','kannazuki')
print(my_tuple[2:])  #output: ('kanao','yuzuki')


# nested
nested_tuple = (1,2,(3,4))
print(nested_tuple)


