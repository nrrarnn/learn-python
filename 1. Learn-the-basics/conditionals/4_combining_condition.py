# Combining Conditions:
# Python allows you to combine multiple conditions using logical operators:

# and: Both conditions must be true.
# or: At least one condition must be true.
# not: Inverts the truth value of the condition.

x = 10
y = 20

# Using 'and'
if x > 5 and y > 15:
    print("Both conditions are true")

# Using 'or'
if x > 15 or y > 15:
    print("At least one condition is true")

# Using 'not'
if not x > 15:
    print("x is not greater than 15")
