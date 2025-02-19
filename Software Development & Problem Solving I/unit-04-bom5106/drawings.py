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

def draw_pixels(sequence):
    index = 0
    while index < len(sequence):
        val = sequence[index]
        if val == '0':
            draw_pixel('black')
        elif val == '1':
            draw_pixel('white')
        elif val == '2':
            draw_pixel('red')
        elif val == '3':
            draw_pixel('yellow')
        elif val == '4':
            draw_pixel('orange')
        index += 1
def main():
    initalize()
    turtle.tracer(False)
    draw_pixels('00000000000000000000')
    next_row()
    draw_pixels('01111111111111111110')
    next_row()
    draw_pixels('01111111111111111110')
    next_row()
    draw_pixels('01111111100111111110')
    next_row()
    draw_pixels('01111111033011111110')
    next_row()
    draw_pixels('01111110333301111110')
    next_row()
    draw_pixels('01000000333300000010')
    next_row()
    draw_pixels('01033333333333333010')
    next_row()
    draw_pixels('01104333033033340110')
    next_row()
    draw_pixels('01110433033033401110')
    next_row()
    draw_pixels('01111043033034011110')
    next_row()
    draw_pixels('01111043333334011110')
    next_row()
    draw_pixels('01110433333333401110')
    next_row()
    draw_pixels('01110433333333401110')
    next_row()
    draw_pixels('01104334400443340110')
    next_row()
    draw_pixels('01104440011004440110')
    next_row()
    draw_pixels('01044001111110044010')
    next_row()
    draw_pixels('01000111111111100010')
    next_row()
    draw_pixels('01111111111111111110')
    next_row()
    draw_pixels('00000000000000000000')
    turtle.tracer(True)
    input()

if __name__ == '__main__':
    main()