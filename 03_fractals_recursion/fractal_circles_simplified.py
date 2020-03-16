import turtle


def draw_circle(head, x, y, radius, color="#000"):
    head.penup()
    head.goto(x, y)
    head.pendown()
    head.speed(0)
    head.color(color)
    head.circle(radius)
    return head


def draw_pattern(tess, x, y, radius, thresh=2., color="#000"):
    if radius < thresh: return tess

    x_left = x
    x_right = x
    y_origin = y
    radius_origin = radius
    while(radius > thresh):
        x_left -= radius
        x_right += radius

        radius /= 2.
        y += radius
        tess = draw_circle(tess, x_left, y, radius, color)
        tess = draw_circle(tess, x_right, y, radius, color)
    return draw_pattern(tess, x, y_origin + radius_origin / 2., radius_origin/2, thresh, color)


def draw_patterns(tess, x, y, radius, thresh=2, color="#000"):
    if radius <= thresh: return tess

    x_left = x_right = x
    radius_origin = radius
    y_origin = y
    while(radius > thresh):
        x_left -= radius
        x_right += radius
        radius /= 2.
        y += radius
        tess = draw_pattern(tess, x_left, y, radius, thresh, color)
        tess = draw_pattern(tess, x_right, y, radius, thresh, color)
    return draw_patterns(tess, x, y_origin + radius_origin/2., radius_origin/2., thresh, color)


if __name__ == '__main__':
    width = 1080
    height = 720
    turtle.setup(width, height)

    screen = turtle.Screen()
    screen.bgcolor("#000")
    screen.title("Fractal Circles")

    tess = turtle.Turtle(shape="turtle", visible=False)

    radius = 200.
    x = 0
    y = -radius
    thresh = 2.
    tess = draw_circle(tess, x, y, radius, "#4e4e4e")
    tess = draw_pattern(tess, x, y, radius, thresh=thresh, color="#4e4e4e")
    tess = draw_patterns(tess, x, y, radius, thresh, "#fff")

    screen.exitonclick()
