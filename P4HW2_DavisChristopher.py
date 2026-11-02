# Christopher Davis
# November 1, 2026
# P4HW2
# This program calculates weekly pay for multiple employees.

# Pseudocode
# Set the totals and employee count to zero
# Ask for the first employee's name
# Keep processing employees until the name is Done
# Ask for hours worked and hourly pay rate
# Calculate regular pay, overtime pay, and gross pay
# Display each employee's pay information
# Add each employee's pay to the totals
# Count each employee processed
# Ask for the next employee's name
# When Done is entered, display all totals

# Set starting totals
total_overtime_pay = 0
total_regular_pay = 0
total_gross_pay = 0
employee_count = 0
# Request employee information
name = input("Enter employee name: ")
while name != "Done":

    hours = float(input("Enter number of hours worked: "))
    rate = float(input("Enter hourly pay rate: "))

    # Evaluate overtime
    if hours > 40:
        # Calculate overtime
        overtime_hours = hours - 40

        # Calculate overtime pay
        overtime_pay = overtime_hours * (rate * 1.5)

        # Calculate salary for regular hours
        regular_pay = 40 * rate

        # Calculate gross pay
        gross_pay = regular_pay + overtime_pay

    else:
        overtime_pay = 0
        overtime_hours = 0
        regular_pay = hours * rate
        gross_pay = regular_pay

    # Display results
    print("------------------------------------------------------------------------------------------")
    print("Employee Name:", name)
    print("Overtime Hours:", overtime_hours)
    print(f'{"Hours Worked":<15}{"Pay Rate":<12}{"OverTime Pay":<15}{"Regular Pay":<15}{"Gross Pay":<15}')
    print("------------------------------------------------------------------------------------------")
    print(f'{hours:<15.2f}{rate:<12.2f}{overtime_pay:<15.2f}{regular_pay:<15.2f}{gross_pay:<15.2f}')

       # Add employee pay to totals
    total_overtime_pay += overtime_pay
    total_regular_pay += regular_pay
    total_gross_pay += gross_pay
    employee_count += 1

        # Ask for the next employee
    name = input('Enter employee name or "Done" to terminate: ') 

 # Display final totals
print()
print("Total number of employees entered:", employee_count)
print(f"Total amount paid for overtime: ${total_overtime_pay:.2f}")
print(f"Total amount paid for regular hours: ${total_regular_pay:.2f}")
print(f"Total amount paid in gross: ${total_gross_pay:.2f}")   