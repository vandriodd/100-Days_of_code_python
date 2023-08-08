"""
    Write a program that works out whether if a given year is a leap year
"""

year = int(input("Which year do you want to check? "))

its_leap = "Leap year." if year % 4 == 0 and year % 100 != 0 or year % 100 == 0 and year % 400 == 0 else "Not leap year."

print(its_leap)
