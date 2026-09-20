# Christopher Davis
# September 20, 2026
# P1HW2
# This program calculates and displays travel expenses.

# Pseudocode
# Ask user to enter budget
# Ask user to enter travel destination
# Ask user to enter amount for gas
# Ask user to enter amount for accommodation
# Ask user to enter amount for food
# Add gas, accommodation, and food expenses
# Subtract total expenses from budget
# Display travel expenses and remaining balance

print("This program calculates and displays travel expenses")
print()

budget = int(input("Enter Budget: "))
print()

destination = input("Enter your travel destination: ")
print()

gas = int(input("How much do you think you will spend on gas? "))
print()

accommodation = int(input("Approximately, how much will you need for accomodation/hotel? "))
print()

food = int(input("Last, how much do you need for food? "))
print()

total_expenses = gas + accommodation + food
remaining_balance = budget - total_expenses

print("----------Travel Expenses----------")
print("Location:", destination)
print("Initial Budget:", budget)
print()
print("Fuel:", gas)
print("Accommodation:", accommodation)
print("Food:", food)
print()
print("Remaining Balance:", remaining_balance)