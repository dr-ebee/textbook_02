"""
Python Programming in Context
Try It Out
Page 28
"""

from turtle import *

def draw_square(side_length):
    """Draw a square. If the turtle is pointed to the right when the function is
    called, then the top right corner of the square will be at the starting
    location of the turtle. At the end of the function, the turtle will be at
    the starting position again, pointed in the same direction.
    
    `side_length` is the length of each side in pixels"""
    forward(side_length)
    right(90)
    forward(side_length)
    right(90)
    forward(side_length)
    right(90)
    forward(side_length)
    right(90)

#################################### 1.23 ######################################
# Modify the draw_half_square function to draw a rectangle whose width is twice
# the side length.

def draw_half_square(side_length):
    """
    ADD A DOC STRING HERE! LOOK AT LINES 11-16 FOR AN EXAMPLE!
    """
    ####### REPLACE THIS WITH YOUR CODE ######
    # (right now, it draws a square, but we want it to draw a rectangle)
    forward(side_length)
    right(90)
    forward(side_length)
    right(90)
    forward(side_length)
    right(90)
    forward(side_length)
    right(90)
    ##########################################

# This code calls the function you will modify:
draw_half_square(50)
