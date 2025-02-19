import turtle
from pixart import *

def assertle(xcor, ycor, pencolor, fillcolor):
    # setup - none
    # invoke
    initalize()
    # analyze
    assert turtle.speed() == 0
    assert turtle.isdown() == False
    assert turtle.heading() == 0
    assert turtle.pensize() == 1
    assert turtle.pencolor() == pencolor
    assert turtle.fillcolor() == fillcolor
    assert round(turtle.xcor()) == xcor
    assert round(turtle.ycor()) == ycor
    #assert turtle.ycor() == int((ROWS/2) * PIXAL_SIZE)



def test_initalize():
    # setup - none
    # invoke
    initalize()
    # analyze
    assertle((-COLS/2) * PIXAL_SIZE, (ROWS/2) * PIXAL_SIZE, 'black','white')

def test_draw_pixel():
    #setup
    initalize()
    #invoke
    draw_pixel('red')
    #analyze
    assertle(int((-COLS/2) * PIXAL_SIZE) + PIXAL_SIZE, (ROWS/2) * PIXAL_SIZE, 'black', 'red')

def test_move():
    #setup
    initalize()
    col = 5
    row = 4
    #invoke
    move(col, row)
    #analye
    assertle((-COLS/2) * PIXAL_SIZE + col * PIXAL_SIZE, (ROWS/2) * PIXAL_SIZE - row * PIXAL_SIZE, turtle.pencolor(), turtle.fillcolor())

def test_draw_row():
    #setup
    initalize()
    col = 5
    row = 4
    num = 8
    #invoke
    draw_row(col, row, num)
    #analye
    assertle((-COLS/2) * PIXAL_SIZE + (col + num) * PIXAL_SIZE, (ROWS/2) * PIXAL_SIZE - row * PIXAL_SIZE, turtle.pencolor(), 'red')

def test_draw_square():
    #setup
    initalize()
    col = 5
    row = 4
    size = 8
    #invoke
    draw_sqaure(col, row, size)
    #analye
    assertle((-COLS/2) * PIXAL_SIZE + (col + size) * PIXAL_SIZE, (ROWS/2) * PIXAL_SIZE - (row + size - 1) * PIXAL_SIZE, turtle.pencolor(), 'green')

def test_draw_rectangle():
    #setup
    initalize()
    col = 5
    row = 4
    col_size = 3
    row_size = 5
    #invoke
    draw_sqaure(col, row, col_size, row_size)
    #analye
    assertle((-COLS/2) * PIXAL_SIZE + (col + col_size) * PIXAL_SIZE, (ROWS/2) * PIXAL_SIZE - (row + row_size - 1) * PIXAL_SIZE, turtle.pencolor(), 'green')