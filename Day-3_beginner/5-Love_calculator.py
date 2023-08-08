"""
    Write a programme that, based on the name of a user(s),
    calculates and displays a love compatibility score
"""

print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
names = (name1 + name2).lower()

true = "true"
love = "love"
true_s = 0
love_s = 0

for letter in true:
    true_s += names.count(letter)

for letter in love:
    love_s += names.count(letter)

love_score = int(str(true_s) + str(love_s))

if love_score < 10 or love_score > 90:
    message = f"Your score is {love_score}, you go together like coke and mentos."
elif 40 <= love_score <= 50:
    message = f"Your score is {love_score}, you are alright together."
else:
    message = f"Your score is {love_score}."

print(message)
