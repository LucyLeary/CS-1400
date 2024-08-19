from turtle import *
from random import randint

# CS 1400 Assignment 2. Written by David Johnson and Lucy Leary
# This code, as it is now or after modification, may not be shared or uploaded to any public site.
# It may be uploaded to the course assignment submission system.

window = Screen()
drawing_turtle = Turtle()

# Draw a square with a Python turtle.


def draw_square():
    for side in range(4):
        drawing_turtle.forward(20)
        drawing_turtle.left(90)


# Draw a wall of five blocks with a little distance between each one.
def draw_wall():
    for count in range(5):
        draw_square()
        drawing_turtle.penup()
        drawing_turtle.forward(40)
        drawing_turtle.pendown()


# Move to the top of the screen and draw a wall
drawing_turtle.penup()
drawing_turtle.goto(-140, 250)
drawing_turtle.pendown()
draw_wall()

# Draw a simple face with a head, hair, a mouth, and two eyes.


def draw_face():
    # Draw a head.
    drawing_turtle.left(90)
    drawing_turtle.circle(80)
    # Draw eyes.
    drawing_turtle.left(90)
    drawing_turtle.penup()
    drawing_turtle.forward(40)
    drawing_turtle.pendown()
    drawing_turtle.circle(10)
    drawing_turtle.penup()
    drawing_turtle.forward(80)
    drawing_turtle.pendown()
    drawing_turtle.circle(10)
    # Draw a mouth.
    drawing_turtle.left(90)
    drawing_turtle.penup()
    drawing_turtle.forward(30)
    drawing_turtle.pendown()
    drawing_turtle.circle(40, 180)
    # Draw hair.
    drawing_turtle.penup()
    drawing_turtle.forward(110)
    drawing_turtle.left(90)
    drawing_turtle.forward(40)
    drawing_turtle.pendown()
    drawing_turtle.right(45)
    for count in range(5):
        drawing_turtle.forward(60)
        drawing_turtle.right(180)
        drawing_turtle.forward(60)
        drawing_turtle.right(202.5)


# Move to the top left and draw a face.
drawing_turtle.penup()
drawing_turtle.goto(-120, 110)
drawing_turtle.setheading(0)
drawing_turtle.pendown()
draw_face()

# Move to the top right and turn 45 degrees and draw a face.
drawing_turtle.penup()
drawing_turtle.goto(120, 110)
drawing_turtle.setheading(-45)
drawing_turtle.pendown()
draw_face()

# Draw a fence post.


def draw_fence():
    drawing_turtle.color("black", "brown")  # Set fill color of fence.
    drawing_turtle.begin_fill()
    drawing_turtle.pendown()
    drawing_turtle.forward(10*(2**.5))
    drawing_turtle.left(90)
    drawing_turtle.forward(80)
    drawing_turtle.left(45)
    drawing_turtle.forward(10)
    drawing_turtle.left(90)
    drawing_turtle.forward(10)
    drawing_turtle.left(45)
    drawing_turtle.forward(80)
    drawing_turtle.left(90)
    drawing_turtle.end_fill()
    drawing_turtle.penup()
    drawing_turtle.forward(30)


# Draw a bar across a fence post.
def draw_bar():
    drawing_turtle.color("black", "brown")  # Set fill color of fence bars.
    drawing_turtle.begin_fill()
    drawing_turtle.pendown()
    drawing_turtle.forward(320)
    drawing_turtle.left(90)
    drawing_turtle.forward(15)
    drawing_turtle.left(90)
    drawing_turtle.forward(320)
    drawing_turtle.left(90)
    drawing_turtle.forward(15)
    drawing_turtle.end_fill()
    drawing_turtle.penup()


# Draw a flower.
def draw_flower():
    drawing_turtle.pendown()  # Draw the stem of a flower.
    drawing_turtle.pensize(5)
    drawing_turtle.pencolor("green")
    drawing_turtle.forward(40)
    drawing_turtle.penup()  # Set up location of petals.
    drawing_turtle.forward(10)
    drawing_turtle.left(110)
    for count in range(9):
        drawing_turtle.color("black", "blue")  # Set fill color of flower petals.
        drawing_turtle.begin_fill()
        drawing_turtle.pendown()
        drawing_turtle.circle(5)
        drawing_turtle.right(40)
        drawing_turtle.penup()
        drawing_turtle.forward(10)
        drawing_turtle.end_fill()


# Draw a five point star.
def draw_star():
    drawing_turtle.left(10)
    drawing_turtle.pensize(2)
    drawing_turtle.color("black", "yellow")  # Set outer triangle color of stars.
    drawing_turtle.begin_fill()
    for count in range(5):
        drawing_turtle.forward(25)
        drawing_turtle.left(144)
    drawing_turtle.end_fill()


# Draw a crescent moon.
def draw_moon():
    drawing_turtle.pendown()
    drawing_turtle.circle(60, 207.5)
    drawing_turtle.penup()
    drawing_turtle.circle(60, 152.5)
    drawing_turtle.left(30)
    drawing_turtle.pendown()
    drawing_turtle.circle(61, 147.5)


# Draw a scene using the five functions above.
def draw_moonlit_landscape():
    # Draw fence posts using draw_fence function, and then draw bars across the posts.
    drawing_turtle.penup()
    drawing_turtle.goto(-150, -150)
    drawing_turtle.setheading(0)
    for count in range(10):
        draw_fence()
    drawing_turtle.goto(-170, -100)
    drawing_turtle.setheading(0)
    draw_bar()
    drawing_turtle.goto(-170, -130)
    drawing_turtle.setheading(0)
    draw_bar()
    # Draw a flower.
    drawing_turtle.goto(200, -150)
    drawing_turtle.setheading(90)
    draw_flower()
    # Draw the moon.
    drawing_turtle.penup()
    drawing_turtle.goto(150, 90)
    drawing_turtle.setheading(200)
    draw_moon()
    # Draw some stars at random positions.
    for count in range(10):
        drawing_turtle.penup()
        random_x_value = randint(-180, 110)
        random_y_value = randint(-60, 20)
        drawing_turtle.goto(random_x_value, random_y_value)
        drawing_turtle.pendown()
        draw_star()


draw_moonlit_landscape()

drawing_turtle.speed(0)  # Make tutle go faster.
drawing_turtle.hideturtle()  # Get rid of the arrow showing the turtle location.

window.exitonclick()
