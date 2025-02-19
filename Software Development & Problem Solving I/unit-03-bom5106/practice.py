def convert_height():
    height = int(input("Enter your height in inches: "))
    print ("You are ", height//12,"'", height%12,'" tall', sep="")

def convert_distance():
    kilometers = float(input("Enter the kilometers: "))
    miles = kilometers // 1.609344
    miles_remainder = kilometers / 1.609344 - miles
    
    feet = miles_remainder * 5280
    
    inches = (feet - int(feet)) * 12 
    print (kilometers,"kilometers is", int(miles), "miles,", int(feet), "feet,", int(inches),"inches", sep=" ")

import turtle

def snow_man(x, y, radius, pencolor,fillColor):
    turtle.up()
    turtle.goto(x,y)
    turtle.setheading(0)
    turtle.pencolor(pencolor)
    turtle.fillcolor(fillColor)
    turtle.down()
    turtle.begin_fill()
    turtle.circle(radius)
    turtle.end_fill()

def rectangle(x, y, width, height, pencolor, fillcolor):
    turtle.up()
    turtle.goto(x, y)
    turtle.pencolor(pencolor)
    turtle.fillcolor(fillcolor)
    turtle.begin_fill()
    turtle.down()
    turtle.forward(width)
    turtle.left(90)
    turtle.forward(height)
    turtle.left(90)
    turtle.forward(width)
    turtle.left(90)
    turtle.forward(height)
    turtle.left(90)
    turtle.up()
    turtle.end_fill()

def main():
    convert_height()
    convert_distance()
    turtle.speed(0)
    turtle.tracer(False)
    rectangle(-500, -200, 950, 600, "cyan", "cyan")
    
    snow_man(0,100, 50, "black", "white")
    
    snow_man(0,-50, 75, "black", "white")
    
    snow_man(0,-200, 100, "black", "white")
    
    turtle.tracer(True)
    input()
main()