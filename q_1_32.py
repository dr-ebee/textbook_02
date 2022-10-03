"""
Python Programming in Context
Try It Out
Page 32
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

#################################### 1.32 ######################################
# Write a draw_spiral function to turn LESS than 90 degrees for each iteration

def draw_spiral(max_side):
    """
    ADD A DOC STRING HERE!
    """
    for side_length in range(1, max_side + 1, 5):
        forward(side_length)
        right(90)

# Call your function here:
