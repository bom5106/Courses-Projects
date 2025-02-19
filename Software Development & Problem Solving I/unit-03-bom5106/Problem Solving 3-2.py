import random
import turtle

"""
Problem Solving 1
"""
#An error occurs when a program that you are executing behaves in a way that is unwanted

#Syntax Error - occurs as a result of breaking the rules of the programming language
#Example: Missing parentheses in call to print
#While working on the stick person.py file, forgot to put the parentheses for up

#Runtime Error - occurs when you are executing the program and it CRASHES
#Example: Trying to call a function that does not exist or using '+' to add a string to an integer

#Semantic Error - nastiest of the bunch; the program is sybtactically correct and runs without crashing, but it produces the wrong result
#Example: an incorrectly implemented formula for computing the area of a triangle returns the wrong value or the turtle draws the wrong image

"""
Problem Solving 2
"""
a = random.randint(-300, 300)
b = random.randint(-300, 300)
turtle.goto(a,b)
number = random.random() * 0.5 + 0.5
angle = random.random() * 360
turtle.left(angle)

"""
Problem Solving 3
"""
turtle.color(1,0,0)
turtle.fillcolor(1,0,0)

turtle.color(0,0,1)
turtle.fillcolor(1,0,1)

r=random.random()
g=random.random()
b=random.random()
turtle.color(r,g,b)
turtle.fillcolor(random.random(), random.random(), random.random())

"""
Problem Solving 4
"""
def draw_star(length):
    turtle.forward(length)
    turtle.left(144)
    turtle.forward(length)
    turtle.right(72)
    turtle.forward(length)
    turtle.left(144)
    turtle.forward(length)
    turtle.right(72)
    turtle.forward(length)
    turtle.left(144)
    turtle.forward(length)
    turtle.right(72)
    turtle.forward(length)
    turtle.left(144)
    turtle.forward(length)
    turtle.right(72)
    turtle.forward(length)
    turtle.left(144)
    turtle.forward(length)
    turtle.right(72)

def main():
    draw_star(100)
main()