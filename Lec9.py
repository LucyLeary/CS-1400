import turtle
window = turtle.Screen()


def positive_only(number):
    if number > 0:
        return number
    else:
        return 0


def main():
    print(positive_only(13))
    this_list = ["single", 2, 4, 1, 3]
    print(this_list[0:len(this_list)])
    this_list.append(2)
    this_list = this_list + [12, 2.12, 1, "painting my nails"]
    print(type(this_list[7:9]))
    print(this_list)

    for value in range(1, 4):
        for number in range(1, 3):
            print(number * value)

    worker = turtle.Turtle()
    worker.speed(0)
    # worker.color("red", "pink")
    for y in range(-200, 201, 50):
        for x in range(y, 201, 50):
            for radius in range(5, 25, 5):
                worker.penup()
                worker.setpos(x, y)
                # worker.begin_fill()
                worker.pendown()
                worker.circle(radius)
                # worker.end_fill()


if __name__ == "__main__":
    main()

window.exitonclick()
