# This project was conceived and written by Benjamin Kendall and Ellen Rodberg.
# Our goal was to have fun while exploring a new python library.
# pizza_time.py leverages the turtle and random libraries in order to draw a slice of pizza with randomized placement of toppings touching the slice.
# Enjoy a hot digital slice on us!


                # __________._______________________  _____     ___________.___   _____  ___________ #
                # \______   \   \____    /\____    / /  _  \    \__    ___/|   | /     \ \_   _____/ #
                #  |     ___/   | /     /   /     / /  /_\  \     |    |   |   |/  \ /  \ |    __)_  #
                #  |    |   |   |/     /_  /     /_/    |    \    |    |   |   /    Y    \|        \ #
                #  |____|   |___/_______ \/_______ \____|__  /____|____|   |___\____|__  /_______  / #
                #                       \/        \/       \/_____/                    \/        \/  #

#checking new branch
import turtle
import random

turtle.Screen().bgcolor('black')
t = turtle.Turtle()
t.speed(0)


class Slice():
    
    

    def __init__(self, position, turtle_obj, base, *toppings):
        self.position = position
        self.turtle_obj = turtle_obj
        self.base = base
        self.toppings = toppings

        self.tri_point1=(0.0,0.0)
        self.tri_point2=(0.0,0.0)
        self.tri_point3=(0.0,0.0)

    def draw(self):
        
        def draw_triangle(turtle_obj,base,color1='Saddle brown',color2='pale goldenrod'):
            


            turtle_obj.goto(self.position[0],self.position[1])
            turtle_obj.color(color1,color2)
            turtle_obj.begin_fill()

            turtle_obj.forward(base)
            turtle_obj.left(115)
            self.tri_point1 = turtle_obj.pos()

            turtle_obj.forward(base*1.2)
            turtle_obj.left(130)
            self.tri_point2 = turtle_obj.pos()

            turtle_obj.forward(base*1.2)
            turtle_obj.left(115)
            self.tri_point3 = turtle_obj.pos()

            turtle_obj.end_fill()

        def draw_crust(turtle_obj,base,color1='Saddle brown',color2='Saddle Brown'):
            

            turtle_obj.goto(self.position[0],self.position[1])
            turtle_obj.color(color1,color2)
            turtle_obj.begin_fill()

            turtle_obj.forward(base)
            turtle_obj.left(295)
            
            turtle_obj.forward(base/7)
            turtle_obj.left(245)
            
            turtle_obj.forward(base+(base*(1/7.2)))
            turtle_obj.left(245)
           
            turtle_obj.forward(base/7)
            
            turtle_obj.end_fill()

        def draw_toppings(toppings):

            def draw_circle(turtle_obj, size, color1='orange', color2='brown'):

                turtle_obj.color(color1, color2)
                turtle_obj.begin_fill()
                turtle_obj.circle(size,360)
                turtle_obj.end_fill()

            def draw_shrimp(turtle_obj, size, color1='pink', color2='lightpink'):

                turtle_obj.color(color1, color2)
                turtle_obj.begin_fill()
                turtle_obj.circle(size,150)
                turtle_obj.forward(25)
                turtle_obj.left(180)
                turtle_obj.circle((size/1.5),100)
                turtle_obj.end_fill()

            def triangle_area(x1,y1,x2,y2,x3,y3):
                return abs((x1*(y2-y3) + x2 * (y3-y1) + x3 * (y1-y2)) / 2.0)
            
            def check_point_in_triangle( x, y, x1=self.tri_point1[0], y1=self.tri_point1[1], x2=self.tri_point2[0], y2=self.tri_point2[1], x3=self.tri_point3[0], y3=self.tri_point3[1] ):
                
                A  = triangle_area(x1, y1, x2, y2, x3, y3)
                A1 = triangle_area(x, y, x2, y2, x3, y3)
                A2 = triangle_area(x1, y1, x, y, x3, y3)
                A3 = triangle_area(x1, y1, x2, y2, x, y)

                if A == A1 + A2 + A3:
                    return True
                else:
                    return False

            if 'pepperoni' in toppings:
                pepperoni_count = 0
                while pepperoni_count < 10:
                    x = random.randint(-1000,1000)
                    y = random.randint(-1000,1000)

                    accurate = check_point_in_triangle(x,y)
                    if accurate == True:
                        self.turtle_obj.penup()
                        self.turtle_obj.goto(x, y)
                        self.turtle_obj.pendown()
                        draw_circle(self.turtle_obj, random.randint(20, 22))
                        pepperoni_count += 1

            if 'shrimp' in toppings:
                shrimp_count = 0
                while shrimp_count < 10:
                    x = random.randint(-1000,1000)
                    y = random.randint(-1000,1000)

                    accurate = check_point_in_triangle(x,y)
                    if accurate == True:
                        self.turtle_obj.penup()
                        self.turtle_obj.goto(x, y)
                        self.turtle_obj.pendown()
                        draw_shrimp(self.turtle_obj, random.randint(13, 15))
                        shrimp_count += 1


        draw_triangle(self.turtle_obj,self.base) 
        draw_crust(self.turtle_obj,self.base)
        draw_toppings(self.toppings)
        turtle.done()
        self.turtle_obj.hideturtle()
    
slice1 = Slice((-200,-200), t, 400, 'pepperoni', 'shrimp')
slice1.draw()
turtle.done()


# Follow up:

# Currently check_point_in_triangle() only checks whether the starting point for drawing the pepperoni is within the triangle...
# This means some pepperoni slices are hanging off the slice. Ultimately we'd like more than 50% of each slice to be within the bounds of the triangle.
# We would also like to implement a gui before drawing the slice, which allows us to input the size of the slice, the number of pepperonis, and eventually more topping options!

