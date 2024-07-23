# This project was conceived and written by Benjamin Kendall and Ellen Rodberg.
# Our goal was to have fun while exploring a new python library.
# pizza_time.py leverages the turtle and random libraries in order to draw a slice of pepperoni pizza with randomized placement of pepperonis touching the slice.
# Enjoy a hot digital slice on us!


                # __________._______________________  _____     ___________.___   _____  ___________ #
                # \______   \   \____    /\____    / /  _  \    \__    ___/|   | /     \ \_   _____/ #
                #  |     ___/   | /     /   /     / /  /_\  \     |    |   |   |/  \ /  \ |    __)_  #
                #  |    |   |   |/     /_  /     /_/    |    \    |    |   |   /    Y    \|        \ #
                #  |____|   |___/_______ \/_______ \____|__  /____|____|   |___\____|__  /_______  / #
                #                       \/        \/       \/_____/                    \/        \/  #



import turtle
import random
import class_Slice

# creating our background: 
turtle.Screen().bgcolor('black')

# creating our turtle object and setting its speed:
t = turtle.Turtle()
t.speed(0)

slice1 = class_Slice.Slice((-200,-200), t, 400, 'shrimp')
slice1.draw()

# prevent the window from automatically closing when finished. 
turtle.done()


# Follow up:

# Currently check_point_in_triangle() only checks whether the starting point for drawing the pepperoni is within the triangle...
# This means some pepperoni slices are hanging off the slice. Ultimately we'd like more than 50% of each slice to be within the bounds of the triangle.
# We would also like to implement a gui before drawing the slice, which allows us to input the size of the slice, the number of pepperonis, and eventually more topping options!

