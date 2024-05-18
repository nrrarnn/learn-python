# To define a function in Python, you use the def keyword, followed by the function name and parentheses () which may include parameters.

def function_name(parameters):
    """
    Optional: This is a docstring. It describes the function.
    """
    # Function body
    # Code to be executed
    return parameters
  
print(function_name("hallo"))  #Output : hallo


def f(x):
  hasil = 2 * x + 1
  return hasil
y = f(2)

print(y)


# fungsi kuadrat
def kuadrat(x):
  return x ** 2

hasil = kuadrat(8)
print(hasil)

def fungsi_aritmatika(angka_1,angka_2):
  tambah = angka_1 + angka_2
  kurang = angka_1 - angka_2
  kali   = angka_1 * angka_2
  bagi   = angka_1 / angka_2
  
  return tambah,kurang,kali,bagi

ta,ku,ka,ba = fungsi_aritmatika(8,16)

print(f"Tambah = {ta}\nKurang = {ku}\nKali = {ka}\nBagi = {ba}")


#  Default argument function

def say_hello(nama="arin"):
  print(f"hello {nama}")
  
say_hello()  #hello arin
say_hello("Kanna") #hello Kanna


def aritmatika(input1=2,input2=3,input3=4):
  return input1 + input2 + input3

print(aritmatika(input3=10))