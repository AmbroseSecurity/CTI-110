# Christopher Davis
# October 160, 2026
# P3LAB
# This program calculates dollars and coins from an amount of money.

# Pseudocode
# Ask the user to enter an amount of money
# Change the money amount into cents
# Calculate the number of dollars
# Calculate the number of quarters
# Calculate the number of dimes
# Calculate the number of nickels
# Calculate the number of pennies
# Display only the dollars and coins needed

money = float(input("Enter an amount of money: "))

# Convert money to cents
cents = round(money * 100)

# Calculate dollars
dollars = cents // 100
cents = cents - dollars * 100

# Calculate quarters
quarters = cents // 25
cents = cents - quarters * 25

# Calculate dimes
dimes = cents // 10
cents = cents - dimes * 10

# Calculate nickels
nickels = cents // 5
cents = cents - nickels * 5

# Calculate pennies
pennies = cents

# Display results
if dollars == 1:
    print(dollars, "dollar")
elif dollars > 1:
    print(dollars, "dollars")

if quarters == 1:
    print(quarters, "quarter")
elif quarters > 1:
    print(quarters, "quarters")

if dimes == 1:
    print(dimes, "dime")
elif dimes > 1:
    print(dimes, "dimes")

if nickels == 1:
    print(nickels, "nickel")
elif nickels > 1:
    print(nickels, "nickels")

if pennies == 1:
    print(pennies, "penny")
elif pennies > 1:
    print(pennies, "pennies")