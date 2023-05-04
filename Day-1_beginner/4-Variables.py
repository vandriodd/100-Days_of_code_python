"""
    Write a program that switches the
    values stored in the variables a & b
"""

# Stores the input
a = input("a: ")
b = input("b: ")

# Swap
tmp = a
a = b
b = tmp

# Result
print("a: " + a)
print("b: " + b)
