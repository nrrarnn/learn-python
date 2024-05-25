# QUEUE

# Queue is a collection of items where the addition of items occurs at one end which is commonly referred to as rear and for deletion, occurs at the other end. Or we usually name it “head”. So the concept of this queue uses the proper concept of FIFO which stands for First in First out. In everyday life, this concept is usually analogized as a queue. Where everyone who comes first, then he will be served first. Now this concept is very different from the concept on the stack. However, just like a stack, this class also has several operations.

# Using list

queue = []
check = not queue
print(check)

# enqueue
queue.append(20)
queue.append(30)
queue.append(40)

# dequeue
queue.pop(0)

# Using class

import collections

q = collections.deque()

q.appendleft(2)
q.appendleft(30)
q.appendleft(10)

q.pop()
# delete 2
q.popleft()
# delete 10
print(q)


# Priority queue
import queue
# lowest
priorityQueue = queue.PriorityQueue()

priorityQueue.put(30)
priorityQueue.put(20)
priorityQueue.put(10)
priorityQueue.put(50)

priorityQueue.get()
# will delete value 10 because it is deleted based on the smallest value