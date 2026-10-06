# Christopher Davis
# October 6, 2026
# P2HW1
# Travel expenses

# Get travel information from user
budget = float(input("Enter Budget: "))
destination = input("Enter your travel destination: ")
gas = float(input("How much do you think you will spend on gas? "))
hotel = float(input("How much will you need for accommodation/hotel? "))
food = float(input("How much do you need for food? "))

# Calculate expenses
expenses = gas + hotel + food
balance = budget - expenses

# Display results
print()
print("----------Travel Expenses----------")
print(f'{"Location:":<20}{destination}')
print(f'{"Initial Budget:":<20}${budget:.2f}')
print()
print(f'{"Fuel:":<20}${gas:.2f}')
print(f'{"Accommodation:":<20}${hotel:.2f}')
print(f'{"Food:":<20}${food:.2f}')
print()
print(f'{"Remaining Balance:":<20}${balance:.2f}')