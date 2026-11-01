# Name: Christopher Davis
# Date: November 1, 2026
# Assignment: P4LAB1
# Description: Draw a house using turtle graphics and loops.

# Pseudocode:
# Import the turtle library
# Create a screen and change its background color
# Create a turtle and change its color
# Use a for loop to draw the square
# Move the turtle to the top of the square
# Use a while loop to draw the triangle roof
# Keep the window open

import turtle

# Set up the screen
wn = turtle.Screen()
wn.bgcolor("lightblue")
wn.title("Christopher's Turtle House")

# Set up the turtle
house = turtle.Turtle()
house.color("darkblue")
house.pensize(3)
house.speed(3)

# Draw the square using a for loop
for i in range(4):
    house.forward(150)
    house.left(90)

# Move to the top left corner of the square
house.left(90)
house.forward(150)
house.right(90)

# Draw the triangle roof using a while loop
count = 0

while count < 3:
    house.forward(150)
    house.left(120)
    count = count + 1

# Keep the drawing window open
wn.mainloop()