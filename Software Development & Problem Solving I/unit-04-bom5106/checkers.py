import turtle

PIXAL_SIZE = 30
ROWS = 20
COLS = 20

def initalize():
    turtle.reset()
    turtle.speed(0)
    turtle.up()
    turtle.setheading(0)
    turtle.pensize(1)
    turtle.pencolor('black')
    turtle.fillcolor('white')
    turtle.setpos(-COLS/2 * PIXAL_SIZE, ROWS/2 * PIXAL_SIZE)

def draw_pixel(color):
    turtle.pencolor('black')
    turtle.fillcolor(color)
    sides = 0
    turtle.down()
    turtle.begin_fill()
    while sides < 4:
        turtle.forward(PIXAL_SIZE)
        turtle.right(90)
        sides += 1
    turtle.end_fill()
    turtle.up()
    turtle.forward(PIXAL_SIZE)

def next_row():
    y = turtle.ycor() - PIXAL_SIZE
    x = -COLS/2 * PIXAL_SIZE
    turtle.setpos(x,y)

def red_and_black(number):
    index = 0
    while index < number:
        draw_pixel('black')
        draw_pixel('red')
        index +=1

def black_and_red(number):
    index = 0
    while index < number:
        draw_pixel('red')
        draw_pixel('black')
        index +=1

def main():
    initalize()
    turtle.tracer(False)
    red_and_black(10)
    next_row()
    black_and_red(10)
    next_row()
    red_and_black(10)
    next_row()
    black_and_red(10)
    next_row()
    red_and_black(10)
    next_row()
    black_and_red(10)
    next_row()
    red_and_black(10)
    next_row()
    black_and_red(10)
    next_row()
    red_and_black(10)
    next_row()
    black_and_red(10)
    next_row()
    red_and_black(10)
    next_row()
    black_and_red(10)
    next_row()
    red_and_black(10)
    next_row()
    black_and_red(10)
    next_row()
    red_and_black(10)
    next_row()
    black_and_red(10)
    next_row()
    red_and_black(10)
    next_row()
    black_and_red(10)
    next_row()
    red_and_black(10)
    next_row()
    black_and_red(10)
    next_row()
    turtle.tracer(True)
    input()
if __name__ == '__main__':
    main()