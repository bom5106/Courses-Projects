import turtle

ANGLE = 45

X_LOCATION = -300
Y_LOCATION = -300

def turtle_speed(speed, tracer):
    turtle.speed(speed)
    turtle.tracer(tracer)

def draw_squares(length, pencolor, fillcolor, x,y):
   turtle.up()
   turtle.goto(x, y)
   turtle.down()
   turtle.pencolor(pencolor)
   turtle.fillcolor(fillcolor)
   turtle.begin_fill()
   turtle.forward(length)
   turtle.left(90)
   turtle.forward(length)
   turtle.left(90)
   turtle.forward(length)
   turtle.left(90)
   turtle.forward(length)
   turtle.left(90)
   turtle.up()
   turtle.end_fill()

def change_size(old_length):
    new_length = (old_length/2)*2**0.5
    return new_length

def main():
    turtle_speed(0,False)
    square_side = 600
    
    draw_squares(square_side, "black", "blue", -300,-300)
    new_length = change_size(square_side)
    
    turtle.right(ANGLE)
    draw_squares(new_length, "black", "red", -300, 0)
    new_length=change_size(new_length)

    turtle.left(ANGLE)
    draw_squares(new_length, "black", "yellow", -150, -150)
    new_length=change_size(new_length)

    turtle.right(ANGLE)
    draw_squares(new_length, "black", "cyan", -150, 0)
    new_length=change_size(new_length)

    turtle.left(ANGLE)
    draw_squares(new_length, "black", "orange", -75,-75)
    new_length=change_size(new_length)

    turtle.right(ANGLE)
    draw_squares(new_length, "black", "black", -75,0)
    new_length=change_size(new_length)

    turtle_speed(0,True)
    input()
main()