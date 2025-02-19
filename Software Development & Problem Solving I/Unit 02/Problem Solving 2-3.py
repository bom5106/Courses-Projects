import turtle
"""
Problem Solving 1
"""
def turtle_circle(xcor, ycor, penColor, fillColor, radius):
    turtle.up()
    turtle.goto(xcor, ycor)
    turtle.down()
    turtle.pencolor(penColor)
    turtle.fillcolor(fillColor)
    turtle.begin_fill()
    turtle.circle(radius)
    turtle.end_fill()

"""
Problem Solving 2
"""
def turtle_triangle(x, y, base, penColor, fillColor):
    turtle.up()
    turtle.goto(x, y)
    turtle.pencolor(penColor)
    turtle.fillcolor(fillColor)
    turtle.begin_fill()
    turtle.down()
    turtle.forward(base)
    turtle.left(120)
    turtle.forward(base)
    turtle.left(120)
    turtle.forward(base)
    turtle.left(120)
    turtle.up()
    turtle.end_fill()

def turtle_rectangle(x, y, width, height, pencolor, fillcolor):
    turtle.up()
    turtle.goto(x, y)
    turtle.pencolor(pencolor)
    turtle.fillcolor(fillcolor)
    turtle.begin_fill()
    turtle.down()
    turtle.forward(width)
    turtle.left(90)
    turtle.forward(height)
    turtle.left(90)
    turtle.forward(width)
    turtle.left(90)
    turtle.forward(height)
    turtle.left(90)
    turtle.up()
    turtle.end_fill()


def main():
    turtle_circle(100, 100, "blue", "red", 100)
    turtle_triangle(-200, 200, 55, "yellow", "black")
    turtle_rectangle(50, 50, 150, 200, "red", "green")
    input()

main()