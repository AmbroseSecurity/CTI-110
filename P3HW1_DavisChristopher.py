# Christopher Davis
# October 18, 2026
# P3HW1
# This program calculates six test grades and displays a letter grade.

# Get grades for six modules
mod_1 = float(input('Enter grade for Module 1: '))
mod_2 = float(input('Enter grade for Module 2: '))
mod_3 = float(input('Enter grade for Module 3: '))
mod_4 = float(input('Enter grade for Module 4: '))
mod_5 = float(input('Enter grade for Module 5: '))
mod_6 = float(input('Enter grade for Module 6: '))

# Put grades into a list
grades = [mod_1, mod_2, mod_3, mod_4, mod_5, mod_6]

# Find lowest, highest, total, and average
low = min(grades)
high = max(grades)
total = sum(grades)
avg = total / 6

# Display results
print()
print("----------Results----------")
print("Lowest Grade:", low)
print("Highest Grade:", high)
print("Sum of Grades:", total)
print("Average:", f"{avg:.2f}")

# Determine letter grade from average
if avg >= 90:
    print('Your grade is: A')
elif avg >= 80:
    print('Your grade is: B')
elif avg >= 70:
    print('Your grade is: C')
elif avg >= 60:
    print('Your grade is: D')
else:
    print('Your grade is: F')