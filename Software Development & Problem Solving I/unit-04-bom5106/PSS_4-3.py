import turtle

LETTER_SIZE = 30
GRID_WIDTH = 20
LEFT = -GRID_WIDTH / 2 * LETTER_SIZE
TOP = GRID_WIDTH / 2 * LETTER_SIZE
DEFAULT_FONT = ('Arial', 19, 'normal')
DEFAULT_COLOR = 'dodgerblue'

def draw_sqaure(color):
    return

#4.3.1
def write_letter(letter, color = DEFAULT_COLOR):
    draw_sqaure(color)
    turtle.forward(LETTER_SIZE/2)
    turtle.write(letter, align="conter", font=DEFAULT_FONT)
    turtle.back(LETTER_SIZE / 2)

#4.3.2
def move(x,y):
    return

def write_word_vertical(x,y,word):
    move(x,y)
    for letter in word:
        write_letter(letter)
        turtle.right(90)
        turtle.forward(LETTER_SIZE)
        turtle.left(90)

# PSS 4.3.3
def validate_horizontal(x, y, word):
    result = True
    if x < 0 or x > GRID_WIDTH or y < 0 or y > GRID_WIDTH:
        result = False
    if (x + len(word)) > GRID_WIDTH:
        result = False
    return result

# PSS 4.3.4
command = input("Please enter <X Coord> <Y Coord> <WORD> <H/V>: ")
tokens = command.split()
x = int(tokens[0])
y = int(tokens[1])
word = tokens[2]
if tokens[3].lower() == "h":
    is_horizontal = True
else:
    is_horizontal = False