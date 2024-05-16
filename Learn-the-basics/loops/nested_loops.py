# Nested Loops
# You can use loops inside other loops, which are called nested loops. Each iteration of the outer loop triggers the inner loop to run completely.

for i in range(3):
    for j in range(3):
        print(f"i: {i}, j: {j}")

# Output :
# i: 0, j: 0
# i: 0, j: 1
# i: 0, j: 2
# i: 1, j: 0
# i: 1, j: 1
# i: 1, j: 2
# i: 2, j: 0
# i: 2, j: 1
# i: 2, j: 2
