# Linked List

# A linked list is a data structure which can change during execution
# it is a collection of linked nodes(think of a chain)
# it can be made as long as possible, grow and shrink during execution
# it does not waste the memory


# type of linked List

# singly linked list

# a set of nodes, each containing some data and a link to the next node

# singly list component

# node : self referencing structure
# list: reference to a node
# linked list : list of nodes
#  ---has dedicated head and tail indicators

# Create a singly linked list
# class LinkedList:

class LinkedList:
  def __init__(self):
    self.head =  None
    
  def print_LL(self):
    if self.head is None:
      print("linkedlist is empty!")
    else:
      n = self.head
      while n is not None:
        print(n.data)
        n = n.ref



