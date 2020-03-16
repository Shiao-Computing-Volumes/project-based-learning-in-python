import turtle

if __name__ == '__main__':
    width = 640
    height = 360
    turtle.setup(width, height)

    screen = turtle.Screen()
    screen.bgcolor("#e3e3e3")
    screen.title("Fractal Circles")

    tess = turtle.Turtle(shape="turtle", visible=True)
    tess.color("blue")

    tess.penup()
    size = 20
    for i in range(30):
        tess.stamp()
        size = size + 3
        tess.forward(size)
        tess.left(24)

    screen.exitonclick()
