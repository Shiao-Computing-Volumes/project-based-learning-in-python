import turtle 


def draw_circles_with_radius_variations(head, rate, radius, extent=None, steps=None):
    while (radius > 1):
        radius *= rate
        head.circle(radius, extent, steps)
    return head

def draw_circles_with_position_variations(head, rate, radius, extent=None, steps=None):
    while (radius < 50):
        radius += rate
        head.circle(radius, extent, steps)
    return head


def draw_recursive_circles(head, radius, rate, n):
    for index in range(n):
        radius *= rate

        head.penup()
        head.goto(0, -radius)

        head.down()
        head.circle(radius)


if __name__ == '__main__':
    head = turtle.Turtle(shape="turtle", visible=False)

    rate = 0.25
    radius = 500
    #head = draw_circles_with_radius_variations(head, rate, radius)
    #head.clear()

    rate = 1
    radius = 10
    #head = draw_circles_with_position_variations(head, rate, radius, 45)
    #head.clear()

    radius = 10
    rate = 1.25
    n = 10
    head = draw_recursive_circles(head, radius, rate, n)
