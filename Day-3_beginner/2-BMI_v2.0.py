"""
    Write a program that interprets the Body Mass Index (BMI)
    based on a user's weight and height
"""

height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))

bmi = round(weight / height**2)
message = f"Your BMI is {bmi}, you are "

if bmi < 18.5:
    interpretation= message + f"underweight."
elif bmi < 25:
    interpretation= message[:-4] + f"have a normal weight."
elif bmi < 30:
    interpretation= message + f"slightly overweight."
elif bmi < 35:
    interpretation= message + f"obese."
print(interpretation)
