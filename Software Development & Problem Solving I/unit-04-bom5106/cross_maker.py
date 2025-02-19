import turtle

LETTER_SIZE = 30

GRID_WIDTH = 20
LEFT = -GRID_WIDTH / 2 * LETTER_SIZE
TOP = GRID_WIDTH / 2 * LETTER_SIZE

PIXAL_SIZE = 40
ROWS = 10
COLS = 10

def initalize():
    turtle.reset()
    # turtle.speed(0)
    turtle.up()
    turtle.setheading(0)
    turtle.pensize(1)
    turtle.pencolor('black')
    turtle.fillcolor('blue')
    turtle.setpos(-COLS/2 * PIXAL_SIZE, ROWS/2 * PIXAL_SIZE)
    # turtle.tracer(False)
    
def draw_sqaure(color, x,y):
    turtle.goto(x,y)
    turtle.pencolor('black')
    turtle.fillcolor(color)
    sides = 0
    turtle.down()
    turtle.begin_fill()
    while sides < 4:
        turtle.forward(PIXAL_SIZE)
        turtle.left(90)
        sides += 1
    turtle.end_fill()
    turtle.up()
    turtle.forward(PIXAL_SIZE)

def write_letter(color,x,y,character):
    draw_sqaure(color, x,y)
    turtle.goto(x+(PIXAL_SIZE)/2, y+(PIXAL_SIZE)/8)
    turtle.write(character, align="center", font=('Arial', 19, 'normal'))

def move(col, row):
    xcor = (-COLS/2 * PIXAL_SIZE)
    xcor = xcor + col * PIXAL_SIZE
    ycor = (ROWS/2 * PIXAL_SIZE)
    ycor = ycor - row * PIXAL_SIZE
    turtle.setpos(xcor, ycor)
    return

def main():
    initalize()
    # turtle.tracer(False)

    # write_letter("red",0,0)
    # write_letter("red",0,-PIXAL_SIZE)

    # turtle.tracer(True)

def write_word_vertical(x,y,word):
    move(x,y)
    for letter in word:
        write_letter("red",x,y,letter)
        turtle.right(90)
        turtle.forward(LETTER_SIZE)
        turtle.left(90)

command = input("Please enter <X Coord> <Y Coord> <WORD> <H/V>: ")
tokens = command.split()
x = int(tokens[0])
y = int(tokens[1])
word = tokens[2]
if tokens[3].lower() == "h":
    is_horizontal = True
else:
    is_horizontal = False

write_word_vertical(x, y, word)

input()
s = turtle.getscreen()
s.mainloop()
if __name__ == '__main__':
    main()