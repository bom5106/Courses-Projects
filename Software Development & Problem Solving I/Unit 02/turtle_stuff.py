import turtle

ANGLE = 78

def test_drive():
    turtle.forward(100)
    turtle.left(90)
    turtle.forward(100)
    turtle.setheading(180)
    turtle.forward(100)
    turtle.up()
    turtle.goto(50,50)
    turtle.down()
    turtle.circle(25)

def turtle_state():
    print(turtle.isdown())
    print(turtle.heading())
    print(turtle.xcor(), turtle.ycor())
    print()

def square(size, ANGLE, penSize, penColor, fillColor):
    turtle.left(ANGLE)
    turtle.down()
    turtle.pensize(penSize)
    turtle.pencolor(penColor)
    turtle.fillcolor(fillColor)
    turtle.begin_fill()
    turtle.forward(size)
    turtle.right(90)
    turtle.forward(size)
    turtle.right(90)
    turtle.forward(size)
    turtle.right(90)
    turtle.forward(size)
    turtle.right(90)


def main():
    turtle.speed(0)
    turtle_state()
    square(100, 54, 4, "red", "yellow")
    square(200, 23, 6, "green", "cyan")
    square(300, 5, 8, "orange", "blue")
    turtle_state()
    input()

main()