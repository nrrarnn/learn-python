# lambda 
# A lambda function in Python is a way to define a small anonymous function using the lambda keyword. They are often used for simple and short tasks, where defining a function by def may feel redundant. Lambda functions are also referred to as “anonymous functions” because they have no name.


# lambda args:expression

kuadrat = lambda number:number**2

print(kuadrat(3))

data_list = ['arin','kannazuki','kanao']
data_list.sort(key=lambda nama:len(nama))

print(data_list)

data_list_num = [1,4,5,6,3,8]

data_list_num_new = list(filter(lambda x:x<6,data_list_num))
data_list_num_new.sort()

print(data_list_num_new)

genap = list(filter(lambda x:x%2==0,data_list_num))
print(genap)
ganjil = list(filter(lambda x:x%2==1,data_list_num))
print(ganjil)