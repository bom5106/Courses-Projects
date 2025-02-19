"""
Draws a sky filled with stars and planets.

@author
"""
import random
import turtle

def tweak(speed, tracer):
    """
    Adjust the turtle's speed and tracer settings so that it can be sped up
    or slowed down as needed for visual debugging.
    """
    turtle.speed(speed)
    turtle.tracer(tracer)

def random_yellow():
    """
    Sets the turtle's fill color to a random shade of yellow using RGB values.
    """
    # the random.random() function returns a floating point value between
    # 0.1 and 1.0. This expression guarantees that the red value will be
    # between 0.5 and 1.0.
    red = 0.5 + random.random() * 0.5
    green = red
    blue = red / 2

    # the turtle color can be set using RGB values ranging from 0.0 to 1.0. In
    #  this case the red and green values are between 0.5 and 1.0 and the blue
    # value is half the value - this guarantees a shade of yellow.
    turtle.color(red, green, blue)
    turtle.fillcolor(red, green, blue)

def random_move():
    """
    Moves the turtle to a random location and orientation on the screen.
    """
    """
    Syntax Error
    Missing ',' in between -1000 & 1000 in y = random
    Showing the red line that missing character
    """
    x = random.randint(-300, 300)
    y = random.randint(-300, 300)
    turtle.goto(x, y) 

    angle = random.randint(0, 360)
    turtle.setheading(angle)

def draw_star(length):
    """
    Draws a star at the turtle's current location and orientation.
    """
    random_yellow()

    turtle.down()
    turtle.begin_fill()

    turtle.forward(length)
    turtle.left(36)
    turtle.forward(length)
    turtle.right(108)

    turtle.forward(length)
    turtle.left(36)
    turtle.forward(length)
    turtle.right(108)

    turtle.forward(length)
    turtle.left(36)
    turtle.forward(length)
    turtle.right(108)

    turtle.forward(length)
    turtle.left(36)
    turtle.forward(length)
    turtle.right(108)

    turtle.forward(length)
    turtle.left(36)
    turtle.forward(length)
    turtle.right(108)

    turtle.end_fill()
    turtle.penup()    

def random_star():
    random_move()
    length=random.randint(10,15)
    draw_star(length)


def draw_world(x, y, radius, color):
    turtle.up()
    turtle.goto(x, y)
    turtle.down()
    turtle.fillcolor(color)
    turtle.begin_fill()
    turtle.circle(radius)
    turtle.end_fill()

def celestial_bodies():
    random_star()
    draw_world()

def main():
    """
    Should ultimately draw a night sky filled with stars and planets.
    """
    turtle.bgcolor("black")
    """
    Semantic Error
    Two tweak (True, 1) & Re-fix to (1, True) 1 is for speed and true is for tracer
    Change 1 to 0 to make it faster
    """
    draw_world(-30,30,30,"red")
    draw_world(-70,-70,50,"yellow")
    draw_world(70,-50,30,"blue")
    turtle.penup()

    tweak(0, False)
    random_star()
    random_star()
    random_star()
    random_star()
    random_star()
    random_star()
    random_star()
    random_star()
    random_star()
    random_star()
    random_star()
    random_star()
    random_star()
    random_star()
    random_star()
    random_star()
    random_star()
    random_star()
    tweak(0,True)
    """
    Runtime Error
    turtle.hide does not exist, need to type as turtle.hideturtle
    Missing turtle.home after pressing enter to continue
    """
    turtle.hideturtle()
    input("Press enter to continue...")
    turtle.home()
main()