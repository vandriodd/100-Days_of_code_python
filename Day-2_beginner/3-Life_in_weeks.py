"""
    Create a program using maths and f-Strings that tells us how many days,
    weeks, months we have left if we live until 90 years old
"""

age = input("What is your current age? ")

days = (90 - int(age)) * 365
weeks = (90 - int(age)) * 52
months = (90 - int(age)) * 12

life = f"You have {days} days, {weeks} weeks, and {months} months left."

print(life)
