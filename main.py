######################################################
# Project: Project 1
# Student Name:  <your name: Fashho, George>
# UIN: <677265024>
# URL: <https://replit.com/@GeorgeFashho/Project-1-George-Fashho#main.py>
######################################################

import turtle
import math
import random

#Naming turtle variables
t1 = turtle.Turtle()
t2 = turtle.Turtle()
t3 = turtle.Turtle()
t4 = turtle.Turtle()
t5 = turtle.Turtle()
t6 = turtle.Turtle()
t7 = turtle.Turtle()
t8 = turtle.Turtle()
t9 = turtle.Turtle()


def draw_background():
    draw_rectangle(t6, -700, 50, 1400, 350, "black", "black", 0, 1)

    #loop and randomization inside def starry_night():

    starry_night()

    draw_circle(t1, -150, 250, 60, 360, 200, "grey", 0, 3)
    draw_circle(t1, -152, 270, 10, 360, 10, "darkgrey", 0, 3)
    draw_circle(t1, -140, 350, 8, 360, 7, "darkgrey", 0, 3)
    draw_circle(t1, -180, 290, 4, 360, 10, "darkgrey", 0, 3)


#Defining a function to draw a shape of a star
def draw_shape():
    for _ in range(5):
        t9.forward(10)
        t9.right(144)


#Function to draw random stars in sky
def starry_night():

    for _ in range(100):
        x = random.randint(-350, 700)
        y = random.randint(100, 350)

        if (x % 2) == 0:
            t9.color("#ffff99")
        else:
            t9.color("white")

        t9.penup()
        t9.goto(x, y)
        t9.pendown()
        draw_shape()


#Defining a function to draw rectangles
#Takes parameters for turtle,x pos, y pos, length, width, pen color, fill color, heading and pen size
def draw_rectangle(t, x, y, length, width, color, fill, heading, pensize):

    t.penup()
    t.goto(x, y)
    t.pendown()

    t.seth(heading)
    t.pensize(pensize)
    t.pencolor(color)
    t.fillcolor(fill)
    t.begin_fill()

    for i in range(2):
        t.forward(length)
        t.left(90)
        t.forward(width)
        t.left(90)

    t.end_fill()


#Defining a function to draw triangles
#Takes parameters for turtle,x pos, y pos, side length, fill color, heading and pen size
def draw_triangle(t, x, y, side_length, color, heading, pensize):

    t.penup()
    t.goto(x, y)
    t.pendown()

    t.seth(heading)
    t.pensize(pensize)
    t.pencolor(color)
    t.fillcolor(color)
    t.begin_fill

    for i in range(3):
        t.forward(side_length)
        t.left(120)

    t.end_fill


#Defining a function to draw circles
#Takes parameters for turtle,x pos, y pos, radius, fill color, heading and pen size
def draw_circle(t, x, y, radius, extent, steps, color, heading, pensize):

    t.penup()
    t.goto(x, y)
    t.pendown()

    t.seth(heading)
    t.pensize(pensize)
    t.pencolor(color)
    t.fillcolor(color)
    t.begin_fill()

    t.circle(radius, extent, steps)
    t.end_fill()


# Define commands to draw a part of the Building
def draw_rod():
    t1.color("brown")
    t1.penup()
    t1.hideturtle()
    t1.goto(-20, 110)
    t1.pendown()
    t1.forward(340)
    t1.circle(10, 180)
    t1.forward(340)
    t1.circle(10, 180)
    t1.penup()
    t1.goto(-30, 120)
    t1.pendown()
    t1.pensize(2)
    t1.forward(360)


def draw_triangle1():
    t1.penup()
    t1.goto(102, 90)
    t1.pendown()

    t1.fillcolor("brown")
    t1.begin_fill()
    t1.forward(90)
    t1.left(-200)
    t1.forward(50)
    t1.left(40)
    t1.forward(50)
    t1.end_fill()


def draw_triangle2():
    t4.fillcolor("brown")
    t4.begin_fill()
    t4.goto(100, 210)
    t4.forward(90)
    t4.left(200)
    t4.forward(50)
    t4.left(-40)
    t4.forward(50)
    t4.end_fill()


#Defining functions to draw top arc of building
def draw_top_arc():
    t5.penup()

    t5.goto(97, 220)

    t5.pendown()

    t5.color("brown")
    t5.fillcolor("brown")
    t5.begin_fill()
    t5.forward(95)
    t5.right(300)
    t5.forward(30)
    t5.right(270)
    t5.forward(60)
    t5.left(30)
    t5.forward(20)
    t5.left(30)
    t5.forward(60)
    t5.right(270)
    t5.forward(30)
    t5.end_fill()
    t5.fillcolor("brown")
    t5.begin_fill()

    draw_triangle(t5, 126, 270, 40, "brown", 360, 1)
    t5.end_fill()
    t5.penup()
    t5.goto(146, 295)
    t5.fillcolor("brown")
    t5.begin_fill()

    t5.pendown()
    t5.circle(10, 360)
    t5.end_fill()


#Group of functions to draw a section of the building
def draw_bottom_half1():
    draw_rectangle(t1, 0, 0, 100, 20, "brown", "brown", 90, 1)
    draw_rectangle(t1, 50, 0, 100, 20, "brown", "brown", 90, 1)
    draw_rectangle(t1, 90, 0, 100, 20, "brown", "brown", 90, 1)
    draw_rectangle(t1, 130, 0, 80, 20, "brown", "brown", 90, 1)
    draw_rectangle(t1, 180, 0, 80, 20, "brown", "brown", 90, 1)
    draw_rectangle(t1, 110, 70, 70, 10, "brown", "brown", 0, 1)
    draw_rectangle(t1, 100, 80, 90, 10, "brown", "brown", 0, 1)
    draw_rectangle(t1, -30, 100, 40, 10, "brown", "brown", 0, 1)
    draw_rectangle(t1, 20, 100, 30, 10, "brown", "brown", 0, 1)
    draw_rectangle(t1, 60, 100, 30, 10, "brown", "brown", 0, 1)
    draw_triangle1()


#Group of functions to draw a section of the building
def draw_bottom_half2():

    draw_rectangle(t1, 220, 0, 100, 20, "brown", "brown", 90, 1)
    draw_rectangle(t1, 270, 0, 100, 20, "brown", "brown", 90, 1)
    draw_rectangle(t1, 320, 0, 100, 20, "brown", "brown", 90, 1)

    draw_rectangle(t1, 200, 100, 30, 10, "brown", "brown", 0, 1)
    draw_rectangle(t1, 250, 100, 30, 10, "brown", "brown", 0, 1)
    draw_rectangle(t1, 290, 100, 40, 10, "brown", "brown", 0, 1)


#Group of functions to draw a section of the building
def draw_object():

    draw_rectangle(t3, 3, 130, 100, 20, "brown", "brown", 90, 1)
    draw_rectangle(t3, 40, 130, 100, 15, "brown", "brown", 90, 1)
    draw_rectangle(t3, 80, 130, 100, 12, "brown", "brown", 90, 1)
    draw_rectangle(t3, 60, 130, 50, 10, "brown", "brown", 90, 1)
    draw_rectangle(t4, -29.5, 200, 40, 20, "brown", "brown", 0, 1)
    draw_rectangle(t4, 20, 200, 30, 20, "brown", "brown", 0, 1)
    draw_rectangle(t4, 60, 200, 30, 20, "brown", "brown", 0, 1)


#Group of functions to draw a section of the building
def draw_top_half2():
    draw_rectangle(t3, 220, 130, 100, 15, "brown", "brown", 90, 1)
    draw_rectangle(t3, 245, 130, 50, 10, "brown", "brown", 90, 1)
    draw_rectangle(t3, 270, 130, 100, 15, "brown", "brown", 90, 1)
    draw_rectangle(t3, 310, 130, 100, 20, "brown", "brown", 90, 1)
    draw_rectangle(t4, 130, 130, 80, 20, "brown", "brown", 90, 1)
    draw_rectangle(t4, 180, 130, 80, 20, "brown", "brown", 90, 1)
    draw_rectangle(t4, 110, 200, 70, 10, "brown", "brown", 0, 1)
    draw_rectangle(t4, 100, 210, 90, 10, "brown", "brown", 0, 1)
    draw_triangle2()
    draw_rectangle(t4, 200, 200, 30, 20, "brown", "brown", 0, 1)
    draw_rectangle(t4, 245, 200, 30, 20, "brown", "brown", 0, 1)
    draw_rectangle(t4, 285, 200, 40, 20, "brown", "brown", 0, 1)
    t4.penup()
    t4.goto(130, 150)
    t4.pendown()
    t4.pensize(3)
    t4.forward(48)


#Group of functions to draw a section of the building
def draw_bottom_arcs():

    t6.penup()
    t6.goto(0, 50)
    t6.pendown()
    t6.right(90)
    t6.pensize(5)
    t6.color("brown")
    t6.circle(15, -180)

    draw_rectangle(t6, 20, 10, 30, 10, "brown", "brown", 90, 3)

    t6.penup()
    t6.goto(300, 50)
    t6.pendown()
    t6.pensize(5)
    t6.circle(15, 180)

    draw_rectangle(t6, 290, 10, 30, 10, "brown", "brown", 90, 3)


#Group of functions to draw background wall of building
def draw_building_background():
    draw_rectangle(t6, -30, 0, 360, 270, "BurlyWood", "BurlyWood", 0, 1)


#Defining a function to draw 2 right angled triangle
def draw_right_angle_triangle1():
    t6.penup()
    t6.goto(25, 230)
    t6.pendown()
    t6.color("brown")
    t6.right(90)
    t6.forward(55)
    t6.left(90)
    t6.forward(35)
    t6.left(120)
    t6.forward(math.sqrt((55**2) + (35**2)))

    t6.penup()
    t6.goto(80, 245)
    t6.pendown()
    t6.forward(30)


#Defining a function to draw 2 right angled triangle
def draw_right_angle_triangle2():
    t7.pensize(3)
    t7.penup()
    t7.goto(265, 230)
    t7.pendown()
    t7.color("brown")
    t7.left(180)
    t7.forward(55)
    t7.right(90)
    t7.forward(35)
    t7.right(120)
    t7.forward(math.sqrt((55**2) + (35**2)))
    t7.penup()
    t7.goto(210, 245)
    t7.pendown()
    t7.forward(30)


#Instructing the turtle to write the title for the project at (x,y) location
def Title():
    t9.penup()
    t9.goto(-300, -50)
    t9.pendown()
    t9.write("Petra, Jordan", False, align="left", font=("Times", 20, "bold"))


#Defining commands to print my name and UIN
def ID_name():

    print("Name: George Fashho")
    print("UIN: 677265024")


#Defining all the functions needed to create the image as well as turtle and screen setups


def main():

    #Screen setup
    s = turtle.Screen()
    s.setup(700, 700)
    turtle.tracer(0)

    #Setting Background Color
    turtle.bgcolor("SandyBrown")

    #List of turtles
    turtles = [t1, t2, t3, t4, t5, t6, t7, t8, t9]

    #For loop to hide and change speed of turtles
    for t in turtles:
        t.hideturtle()
        t.speed(10)

    #Calling all the fucntions to build the whole project
    draw_background()
    draw_building_background()
    draw_bottom_half1()
    draw_bottom_half2()
    draw_rod()
    draw_top_arc()
    draw_object()
    draw_top_half2()
    draw_bottom_arcs()
    draw_right_angle_triangle1()
    draw_right_angle_triangle2()
    draw_circle(t8, -7, 227, 10, 360, 4, "brown", 0, 1)
    draw_circle(t8, 300, 227, 10, 360, 4, "brown", 0, 1)
    ID_name()
    Title()

    turtle.update()


main()

## information for scorers

## on what line number is the required for loop?
## <line 40/47/100/351>

## on what line number is the required use of a random number?
## <line 48/49>

## on what line number is the required use of a conditional statement?
## <line 51>

## on what line number is the required use of a list?
## <line 348>
