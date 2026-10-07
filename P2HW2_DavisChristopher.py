# Christopher Davis
# October 6, 2026
# P2HW2
# This program gets six grades and displays the lowest, highest, sum, and average.

# Get the grades from the user
grade1 = float(input("Enter grade for Module 1: "))
grade2 = float(input("Enter grade for Module 2: "))
grade3 = float(input("Enter grade for Module 3: "))
grade4 = float(input("Enter grade for Module 4: "))
grade5 = float(input("Enter grade for Module 5: "))
grade6 = float(input("Enter grade for Module 6: "))

# Put the grades in a list
grades = [grade1, grade2, grade3, grade4, grade5, grade6]

# Find the lowest, highest, sum, and average
lowest = min(grades)
highest = max(grades)
total = sum(grades)
average = total / len(grades)

# Display the results
print()
print("------------Results------------")
print("Lowest Grade:     ", lowest)
print("Highest Grade:    ", highest)
print("Sum of Grades:    ", total)
print("Average:          ", f"{average:.2f}")
print("--------------------------------")