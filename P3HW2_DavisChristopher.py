# Christopher Davis
# October 18, 2026
# P3HW2
# This program calculates an employee's weekly salary.

# Request employee information
name = input("Enter employee name: ")
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