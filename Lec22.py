import turtle


def un_nest_list(nested_list):
    if type(nested_list) is not list:
        return [nested_list]
    flattened_list = []
    for element in nested_list:
        flattened_list += un_nest_list(element)
    return flattened_list


def optimize_max(nested_integers):
    if type(nested_integers) is int:
        return nested_integers
    biggest_value = None
    for integer in nested_integers:
        new_value = optimize_max(integer)
        if biggest_value is None or new_value > biggest_value:
            biggest_value = new_value
    return biggest_value


def find_smallest(nested_list):
    if type(nested_list) is not list:
        return nested_list
    else:
        smallest = None
        for item in nested_list:
            if smallest is None or find_smallest(item) < smallest:
                smallest = find_smallest(item)
    return smallest


def denest(nested_loop):
    if type(nested_loop) is not list:
        return [nested_loop]
    new_nest = []
    for item in nested_loop:
        new_nest += denest(item)
    return new_nest


def old_search(list, target):
    for item in list:
        if item == target:
            return True
    return False


def search(nested_list, target):
    if type(nested_list) is int:
        return target == nested_list
    for item in nested_list:
        if search(item, target):
            return True
    return False


print(search([1, 2, 3, [45, 6]], 45))

# def snowflake(side_length, fractal_turtle):
#     if side_length < 7:
#         fractal_turtle.forward(side_length * 3)
#         return
#     snowflake(side_length // 3, fractal_turtle)
#     fractal_turtle.left(60)
#     snowflake(side_length // 3, fractal_turtle)
#     fractal_turtle.right(120)
#     snowflake(side_length // 3, fractal_turtle)
#     fractal_turtle.left(60)
#     snowflake(side_length // 3, fractal_turtle)
#
#
# def main():
#     """
#     Provide code to set up and test the spiral and circle
#     fractal code.
#     :return: None.
#     """
#     # Set up the turtle and window
#     fractal_turtle = turtle.Turtle()
#     fractal_turtle.speed(0)
#     myWin = turtle.Screen()
#     fractal_turtle.penup()
#     fractal_turtle.backward(300)
#
#     # Draw the snowflake
#     fractal_turtle.pendown()
#     # draw_spiral(5, 200, fractal_turtle)
#     snowflake(240, fractal_turtle)
#
#     myWin.exitonclick()
#
#
# if __name__ == "__main__":
#     main()
#
#
# def un_nest_list(nested_list):
#     if type(nested_list) != list:
#         return nested_list
#     else:
#         return nested_list[0] + un_nest_list[1:]
#
#
# print(un_nest_list([[0, 1], 2]))
