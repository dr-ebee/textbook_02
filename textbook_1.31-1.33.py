"""
Python Programming in Context
Try It Out
Page 28
Exercises 1.31 - 1.33
"""

from turtle import *

def draw_rectangular_spiral(max_side):
    """Draw a rectangular spiral, starting in the center.
    
    `max_side` is the length of the longest side of the spiral in pixels"""

    # Remember: When range takes 2 parameters, the first parameter is the start
    # and the second parameter is the end. So this range will start at 1 and
    # stop before it gets to max_side + 1 (i.e. it will stop at max_side)
    for side_length in range(1, max_side + 1, 5):
        forward(side_length)
        right(90)

#################################### 1.31 ######################################
# Write a draw_spiral_2 function to turn MORE than 90 degrees for each iteration

def draw_spiral_2(max_side):
    """
    ADD A DOC STRING HERE!
    """
    for side_length in range(1, max_side + 1, 5):
        forward(side_length)
        right(90)

# This code calls the function you will modify:
draw_spiral_2(100)

#################################### 1.32 ######################################
# Write a draw_spiral_3 function to turn LESS than 90 degrees for each iteration

def draw_spiral_3(max_side):
    """
    ADD A DOC STRING HERE!
    """
    for side_length in range(1, max_side + 1, 5):
        forward(side_length)
        right(90)

# Call your function here:


#################################### 1.33 ######################################
# Write a draw_spiral_4 function to use the loop variable as the number of
# degrees to turn.

def draw_spiral_4(max_side):
    """
    ADD A DOC STRING HERE!
    """
    for side_length in range(1, max_side + 1, 5):
        forward(side_length)
        right(90)

# Call your function here:
