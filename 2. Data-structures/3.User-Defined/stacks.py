# Stack

# stack is an organized collection of data, where data can be added and deleted at the end of the data.

# Stack is Last in first out

# the last object in will be the first one out of the stack

# stack implementation

# List

# Stack operation 

# Push
# L.append(e)
# insert an element into the stack
# the input element will become an element in the stack
stack = []
stack.append(20)
stack.append(30)
print(stack)  #output : [20,30]


# Pop
# L.pop()
# remove the top element from the stack
# if the stack is empty it will throw an errorKik untuk menerapkan
stack.pop()
print(stack) #output : [20]



# IsEmpty
# len(L) == 0
stack = []
is_empty = len(stack) == 0
print(is_empty)   #True


# Indexing
stack.append(10)
stack.append(20)
stack.append(30)
stack[-1]    #Output : 30


