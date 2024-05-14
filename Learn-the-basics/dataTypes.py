# Data Types in Python

# Integer(int) 
# Whole numbers, both positive and negative, without decimals.
a = 10
b = 20
print(a + b)  # Output: 30
# Operations: Add (+), subtract (-), multiply (*), divide (/), modulus (%), exponent (**), integer division (//).

# Float 
# Decimal numbers, both positive and negative.
pi = 3.14159
radius = 5
area = pi * (radius ** 2)
print(area)  # Output: 78.53975
# Operations: same as integer

# String (str)
# A sequence of characters enclosed in single (') or double (") quotes.
greeting = "Hello"
name = "Arin"
full_greeting = greeting + ", " + name + "!"
print(full_greeting)  # Output: Hello, Arin!
# Operations: Concatenation (+), repetition (*), indexing ([0]), slicing ([1:4]), built-in methods (e.g., upper(), lower(), split()).


# Boolean (bool)
# A data type that only has two values: True and False.
is_open = True
is_closed = not is_open
print(is_closed)  # Output: False
# Operation: Logic (and, or, not, xor).

# List
# Sequences are mutable and can store various types of data.
fruits = ["apple", "banana", "cherry"]
fruits.append("orange")
print(fruits)  # Output: ['apple', 'banana', 'cherry', 'orange']
# Operations: Indexing ([0]), slicing ([1:3]), add element (append()), remove element (remove()), length (len()).

# Tuple
# An immutable sequence.
point = (2, 3)
x, y = point
print(x, y)  # Output: 2 3
# Operations: Indexing ([0]), slicing ([1:2]), length (len()). Cannot modify or delete elements.

# Dictionary
# An unordered collection of key-value pairs.
student = {"name": "John", "age": 21, "courses": ["Math", "Science"]}
student["age"] = 22
print(student)  # Output: {'name': 'John', 'age': 22, 'courses': ['Math', 'Science']}
# Operations: Access value ([“name”]), add/modify value ([“age”] = 31), delete element (del).

# Set
# An unordered collection of unique elements.
numbers = {1, 2, 3, 4, 5}
numbers.add(6)
print(numbers)  # Output: {1, 2, 3, 4, 5, 6}
# Operations: Adding elements (add()), removing elements (remove()), set operations (union, intersection, difference).

# None Type
value = None
if value is None:
    print("Value is None")  # Output: Value is None


# Complex Numbers
# A complex number that has both real and imaginary parts.
z1 = 1 + 2j
z2 = 3 + 4j
z_sum = z1 + z2
print(z_sum)  # Output: (4+6j)
