"""
    Tip calculator project
"""

# Greeting
print("Welcome to the tip calculator.")

# Questions about the bill
bill = float(input("What was the total bill? "))
tip = int(input("What percentage tip would you like to give? 10, 12 or 15? "))
people = int(input("How many people to split the bill? "))

# Calculate final amount
total_bill = (tip / 100 * bill + bill) / people
final_amount = round(total_bill, 2)

# Show it
result = f"Each person should pay ${final_amount}"
print(result)
