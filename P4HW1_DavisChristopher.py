# Name: Christopher Davis
# Date: November 1, 2026
# Assignment: P4HW1
# Description: Calculate the average test score after dropping the lowest score.

# Pseudocode:
# Ask the user how many scores they want to enter
# Create an empty list to store the scores
# Use a loop to collect the scores
# Check that each score is between 0 and 100
# If a score is invalid, ask the user to enter it again
# Add each valid score to the list
# Find the lowest score
# Remove the lowest score from the list
# Calculate the average of the remaining scores
# Determine the letter grade
# Display the lowest score, modified list, average, and grade

# Ask how many scores the user wants to enter
num_scores = int(input("How many scores do you want to enter? "))
scores = []

# Collect the test scores
for i in range(num_scores):
    score = float(input("Enter score #" + str(i + 1) + ": "))

    while score < 0 or score > 100:
        print("INVALID Score entered!!!!")
        print("Score should be between 0 and 100")
        score = float(input("Enter score #" + str(i + 1) + " again: "))

    scores.append(score)

    # Find and remove the lowest score
lowest_score = min(scores)
scores.remove(lowest_score)

# Calculate the average of the remaining scores
average = sum(scores) / len(scores)

# Determine the letter grade
if average >= 90:
    grade = "A"
elif average >= 80:
    grade = "B"
elif average >= 70:
    grade = "C"
elif average >= 60:
    grade = "D"
else:
    grade = "F"

    # Display the results
print()
print("-------------Results-------------")
print("Lowest Score :", lowest_score)
print("Modified List :", scores)
print("Scores Average :", format(average, ".2f"))
print("Grade :", grade)
print("---------------------------------")