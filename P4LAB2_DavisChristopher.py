# Name: Christopher Davis
# Date: November 1, 2026
# Assignment: P4LAB2
# Description: Display a multiplication table using loops.

# Pseudocode:
# Start the program
# Ask the user to enter an integer
# Check if the number is positive or negative
# If the number is 0 or greater, display the multiplication table
# Use a for loop to multiply the number from 1 to 12
# If the number is negative, display an error message
# Ask the user if they want to run the program again
# If the user enters yes, repeat using a while loop
# If the user enters no, end the program

# Run the program until the user says no
again = "yes"

while again == "yes":
    number = int(input("Enter an integer: "))

    if number >= 0:
        for i in range(1, 13):
            answer = number * i
            print(number, "*", i, "=", answer)
    else:
        print("This program does not accept negative numbers.")

    again = input("Would you like to run the program again? ")

print("Exiting program...")