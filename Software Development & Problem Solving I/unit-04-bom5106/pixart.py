import turtle

PIXAL_SIZE = 50
ROWS = 10
COLS = 10

def initalize():
    turtle.reset()
    turtle.speed(0)
    turtle.up()
    turtle.setheading(0)
    turtle.pensize(1)
    turtle.pencolor('black')
    turtle.fillcolor('white')
    turtle.setpos(-COLS/2 * PIXAL_SIZE, ROWS/2 * PIXAL_SIZE)
    turtle.tracer(False)

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

def red_pixels(number):
    index = 0
    while index < number:
        draw_pixel('red')
        index += 1

#PSS Number 4
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

def move(col, row):
    xcor = (-COLS/2 * PIXAL_SIZE)
    xcor = xcor + col * PIXAL_SIZE
    ycor = (ROWS/2 * PIXAL_SIZE)
    ycor = ycor - row * PIXAL_SIZE
    turtle.setpos(xcor, ycor)
    return

def draw_row(col, row, num_pix, color = 'red'):
    move(col, row)
    for _ in range(num_pix):
        draw_pixel(color)

def draw_sqaure(col, row, size, color = 'green'):
    draw_rectangle(col, row, size, size, color)

def draw_rectangle(col, row, col_size, row_size, color = 'orange'):
    for i in range(row_size):
        draw_row(col, row, col_size, color)
        row += 1

    # pix_drawn = 0
    # while (pix_drawn < num_pix):
    #     draw_pixel(color)
    #     pix_drawn += 1

def main():
    initalize()
    turtle.tracer(False)
    # draw_pixel('red')
    # draw_pixel('orange')
    # draw_pixel('blue')
    # draw_pixel('purple')
    # draw_pixel('yellow')
    # draw_pixel('green')
    
    red_pixels(5)
    next_row()
    red_pixels(7)
    next_row()
    draw_pixels('01234')
    move(5,4)
    draw_pixels('01234')
    draw_row(2,7,5, 'green')
    draw_sqaure(1,9,3)
    draw_rectangle(6,2,3,4,'purple')

    # draw_pixel('purple')
    # draw_pixel('yellow')
    # draw_pixel('red')
    # draw_pixel('orange')
    # draw_pixel('blue')
    

    turtle.tracer(True)
    input()

if __name__ == '__main__':
    main()