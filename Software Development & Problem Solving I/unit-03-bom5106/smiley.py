import turtle

NOSE_PROPORTION = 7
SMILY_SIZE = 150
SMILY_SEPARATION = SMILY_SIZE * 2

def draw_circle(x, y, radius, fillColor):
    turtle.up()
    turtle.goto(x,y)
    turtle.setheading(0)
    turtle.pencolor('black')
    turtle.fillcolor(fillColor)
    turtle.down()
    turtle.begin_fill()
    turtle.circle(radius)
    turtle.end_fill()

def draw_centered_circle(x, y, radius, fillColor):
    # move to center
    turtle.up()
    turtle.goto(x,y)
    turtle.setheading(0)
    turtle.pencolor('black')
    turtle.fillcolor(fillColor)
    # move out to edge (radius)
    turtle.forward(radius)
    # turn left
    turtle.left(90)
    # draw circle
    turtle.down()
    turtle.begin_fill()
    turtle.circle(radius)
    turtle.end_fill()
    turtle.up()
    # turn left
    turtle.left(90)
    # move by radius
    turtle.forward(radius)
    #turn around
    turtle.setheading
    pass
    return

def draw_month(x, y, radius, fillColor):
    # move to center
    turtle.up()
    turtle.goto(x,y)
    turtle.setheading(0)
    turtle.pencolor('black')
    turtle.fillcolor(fillColor)
    # move out to edge (radius)
    turtle.setheading(180)
    turtle.forward(radius)
    # turn left
    turtle.left(90)
    # draw circle
    turtle.down()
    turtle.begin_fill()
    turtle.circle(radius, 180)
    turtle.end_fill()
    turtle.up()
    # turn left
    turtle.left(90)
    # move by radius
    turtle.forward(radius)
    #turn around
    turtle.setheading
    pass
    return

def draw_smiley(x, y, size, eyeColor):
    draw_centered_circle(x, y, size, 'yellow')
    noseSize = size / NOSE_PROPORTION
    draw_centered_circle(x, y, noseSize, 'pink')
    quarter = size / 4
    third = size / 3
    draw_eye(x + third, y + third, quarter, eyeColor)
    draw_eye(x - third, y + third, quarter, eyeColor)
    draw_month(x,y-quarter, size*0.6, 'black')
 
 

def draw_eye(x, y, size, eyeColor):
    draw_centered_circle(x, y, size, 'white')
    draw_centered_circle(x, y, size/2, eyeColor)
    draw_centered_circle(x, y, size/4, 'black')

def main():
    turtle.speed(0)
    turtle.tracer(False)
    draw_smiley(0,0, SMILY_SIZE, 'blue')
    draw_smiley(SMILY_SEPARATION, SMILY_SEPARATION, SMILY_SIZE, 'blue')
    draw_smiley(-SMILY_SEPARATION, SMILY_SEPARATION, SMILY_SIZE, 'green')
    draw_smiley(SMILY_SEPARATION, -SMILY_SEPARATION, SMILY_SIZE, 'red')
    draw_smiley(-SMILY_SEPARATION, -SMILY_SEPARATION, SMILY_SIZE, 'black')
    turtle.tracer(True)   
    input()

main()