import turtle


my_turtle = turtle.Turtle()


def draw_square():
    for _ in range(4):
        my_turtle.forward(100)
        my_turtle.right(90)


draw_square()
turtle.done()
