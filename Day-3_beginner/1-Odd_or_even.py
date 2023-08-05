"""
    Write a program that works out wheter if a given
    number is an odd or even number
"""

number = int(input("Which number do you want to check? "))

number_type = "even" if number % 2 == 0 else "odd"
answer = f"This is an {number_type} number."
print(answer)
