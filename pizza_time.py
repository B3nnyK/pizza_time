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

# creating our background: 
turtle.Screen().bgcolor('black')

# creating our turtle object and setting its speed:
t = turtle.Turtle()
t.speed(1)

# global variables for the corner points of the triangle. 
# These will be updated once the triangle has been drawn:
tri_point1=(0.0,0.0)
tri_point2=(0.0,0.0)
tri_point3=(0.0,0.0)

# defining a function that draws a triangle when passed a turtle object and triangle attributes
# this function will also update the global variables for the corner points of the triangle:
def draw_triangle(turtle_obj,base,color1,color2):
    global tri_point1
    global tri_point2
    global tri_point3


    t.goto(-200,-200)
    turtle_obj.color(color1,color2)
    turtle_obj.begin_fill()

    turtle_obj.forward(base)
    turtle_obj.left(120)
    tri_point1 = t.pos()

    turtle_obj.forward(base)
    turtle_obj.left(120)
    tri_point2 = t.pos()

    turtle_obj.forward(base)
    turtle_obj.left(120)
    tri_point3 = t.pos()

    turtle_obj.end_fill()

def draw_crust(turtle_obj,base,color1,color2):

    t.goto(-200,-200)
    turtle_obj.color(color1,color2)
    turtle_obj.begin_fill()

    turtle_obj.forward(base)
    turtle_obj.left(115)
    tri_point1 = t.pos()

    turtle_obj.forward(base/7)
    turtle_obj.left(65)
    tri_point2 = t.pos()

    turtle_obj.forward(base-(base*(1/9)))
    turtle_obj.left(65)
    tri_point3 = t.pos()

    turtle_obj.forward(base/7)
    turtle_obj.left(115)
    tri_point2 = t.pos()

    turtle_obj.end_fill()


# defining a function that draws a nonagon:
def draw_circle(turtle_obj, size, color1, color2):

    turtle_obj.color(color1, color2)
    turtle_obj.begin_fill()
    turtle_obj.circle(size,360)
    turtle_obj.end_fill()




# drawing triangle:
draw_triangle(t,400, 'Saddle brown', 'pale goldenrod')
draw_crust(t,400,'Saddle brown','Saddle brown')

#defining a function to calculate and return the area of a triangle given the coordinates of 3 points:
def triangle_area(x1,y1,x2,y2,x3,y3):
    return abs((x1*(y2-y3) + x2 * (y3-y1) + x3 * (y1-y2)) / 2.0)



# defining a function that checks to see if a given point(x,y) is within a given triangle made by three points.
# default x,y values for the three triangle points are our global tri_point variables.
# there is almost certainly a more elegant calculus based approach here?:
def check_point_in_triangle( x, y, x1=tri_point1[0], y1=tri_point1[1], x2=tri_point2[0], y2=tri_point2[1], x3=tri_point3[0], y3=tri_point3[1] ):
     A  = triangle_area(x1, y1, x2, y2, x3, y3)
     A1 = triangle_area(x, y, x2, y2, x3, y3)
     A2 = triangle_area(x1, y1, x, y, x3, y3)
     A3 = triangle_area(x1, y1, x2, y2, x, y)

     if A == A1 + A2 + A3:
         return True
     else:
         return False


# drawing pepperonis:
pepperoni_count = 0
while pepperoni_count < 8:
    x = random.randint(-200,200)
    y = random.randint(-200,200)

    accurate = check_point_in_triangle(x,y)
    if accurate == True:
        t.penup()
        t.goto(x, y)
        t.pendown()
        draw_circle(t, random.randint(4, 8), 'orange', 'brown')
        pepperoni_count += 1
    



# prevent the window from automatically closing when finished. 
turtle.done()


# Follow up:

# Currently check_point_in_triangle() only checks whether the starting point for drawing the pepperoni is within the triangle...
# This means some pepperoni slices are hanging off the slice. Ultimately we'd like more than 50% of each slice to be within the bounds of the triangle.
# We would also like to implement a gui before drawing the slice, which allows us to input the size of the slice, the number of pepperonis, and eventually more topping options!
# We also need to made a darker tan trapezoid at the base of the slice to represent the crust.
