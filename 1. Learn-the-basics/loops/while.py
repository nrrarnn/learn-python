# while Loop
# The while loop in Python repeatedly executes a block of code as long as a specified condition is True. The condition is evaluated before executing the block of code, and the loop continues until the condition becomes False.

# Basic Syntax
# while condition:
    # Code block to be executed as long as the condition is True

i = 0
while i < 5:
    print(i)
    i += 1

# Output
# 0
# 1
# 2
# 3
# 4


# Break and continue Statement

# break
# The break statement is used to exit the loop prematurely when a certain condition is met.

for i in range(10):
    if i == 5:
        break
    print(i)

# output :
# 0
# 1
# 2
# 3
# 4

# continue
# The continue statement is used to skip the rest of the code inside the loop for the current iteration and move to the next iteration.

for i in range(10):
    if i % 2 == 0:
        continue
    print(i)

# output :
# 1
# 3
# 5
# 7
# 9





