# Stack

# stack is an organized collection of data, where data can be added and deleted at the end of the data.

# Stack is Last in first out

# the last object in will be the first one out of the stack

# Implementation stack using List

# Stack operation 

# Push
# L.append(e)
# insert an element into the stack
# the input element will become an element in the stack
stack = []
stack.append(20)
stack.append(30)
print(stack)  #output : [20,30]

stacks = []
n = int(input("Limit of stack : "))

def push():
  if len(stacks) == n:
    print('List is full!')
  else:
    element = input("Enter the element : ")
    stacks.append(element)
    print(stacks)

# Pop
# L.pop()
# remove the top element from the stack
# if the stack is empty it will throw an errorKik untuk menerapkan
stack.pop()
print(stack) #output : [20]

def pop_element():
  if not stacks:
    print("stack is empty")
  else:
    e = stack.pop()
    print(f"remove element : {e}")
    print(stacks)


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


# Implementation stack with modules

import collections

stack_2 = collections.deque()
# push
stack_2.append(20)
stack_2.append(50)
# pop
stack_2.pop()

print(stack_2)

import queue

stack_3 = queue.LifoQueue()
# push
stack_3.put(20)
stack_3.put(40)

# pop
stack_3.get()
stack_3.get()

# if stack is empty and u using get, u should using timeout
stack_3.get(timeout=1)


