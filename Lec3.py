# HOW TO USE A TURTLE #

from turtle import *
window = Screen()
my_turtle = Turtle()

def make_square():
    for side in range(4):
        my_turtle.forward(100)
        my_turtle.left(90)
make_square()


# my_turtle.penup()
# my_turtle.setposition(-100, 100)
# my_turtle.pendown()
window.exitonclick()

# HOW TO MAKE A FUNCTION #
def print_words():
    print('hi')
    print('bye')

print_words()
print_words()

