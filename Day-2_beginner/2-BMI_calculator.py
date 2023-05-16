"""
    Write a program that calculates
    the Body Mass Index (BMI)
"""

height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")

print(int((float(weight) / float(height)**2)))
