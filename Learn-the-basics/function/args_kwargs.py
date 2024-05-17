# *args in function

# *args is used to pass a variable number of non-keyword arguments to a function. The *args syntax allows you to accept more arguments than the number of formal parameters you previously defined. With *args, any number of additional arguments can be passed to your function, and these arguments are accessible as a tuple inside the function.

import os
os.system('clear')

def tambah(*data):
  return sum(data)

print(tambah(1,2,3,4,5))
# Output : 15
# **kwargs

# kwargs stands for “keyword arguments”. By using **kwargs, you can accept additional arguments in the form of key-value pairs, and these arguments are accessed as a dictionary within the function.
def data_dict(**kwargs):
  print(kwargs)
  
data_dict(name="arin",height=155,weight=45)
# Output : {name='arin',height=155,weight=45}

# case study
# args & kwargs

def math(*number,**data):
  hasil=0
  if data['option'] == 'add':
    for i in number:
      hasil +=i
  elif data['option'] == 'multifly':
    hasil = 1
    for i in number:
      hasil *=i
  else:
    print("tidak ada operasi")
  return hasil

print(math(1,2,3,4,option='multifly'))

