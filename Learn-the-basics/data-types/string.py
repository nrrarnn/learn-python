# String (str)
# A sequence of characters enclosed in single (') or double (") quotes.
greeting = "Hello "
name = "Arin"
full_greeting = greeting + ", " + name + "!"  # this is concatenation
upper_str = greeting.upper()
split_str = greeting.split()


print(full_greeting)  # Output: Hello, Arin!
print(name[1])  # Output : r     this is indexing start with 0
print(upper_str[1:2]) # Output : E   this is slicing
print(greeting * 2)  # Output : Hello Hello
print(upper_str) # Output : HELLO
print(split_str) # Output : ['Hello']

# Operations: Concatenation (+), repetition (*), indexing ([0]), slicing ([1:4]), built-in methods (e.g., upper(), lower(), split()).


#Format string
print(f"hello {name}!")   # Output : hello Arin!