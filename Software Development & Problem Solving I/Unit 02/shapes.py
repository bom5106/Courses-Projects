import math
def main():
    circle = int(input("Enter the radius: "))
    area = circle * 3.14159
    print("Circle: r =", "{:.1f}".format(circle), ", area =", area)
    print("")
    
    sphere = int(input("Enter the radius: "))
    volume = 4/3 * 3.14159 * sphere**3
    print("Sphere: r =", "{:.1f}".format(sphere), ", area =", volume)
    print("")
    
    height = int(input("Enter the height: "))
    width = int(input("Enter the width: "))
    rectangle_area = height * width
    print("Rectangle: height =", "{:.1f}".format(height), ", width =", "{:.1f}".format(width), ", area =", "{:.1f}".format(rectangle_area))
    print("")
    
    length = int(input("Enter the side length: "))
    square = length * length
    print("Square: side length =", "{:.1f}".format(length),", area =", "{:.1f}".format(square))
    print("")
    
    side_length = int(input("Enter the side length: "))
    height_triangle = int(input("Enter the height: "))
    triangle = 1/2 * side_length * height_triangle
    print("Isosceles Triangle: side = ", "{:.1f}".format(side_length),", height =", "{:.1f}".format(height_triangle), ", area =", "{:.1f}".format(triangle))
    print("")

    equil_side = int(input("Enter the side length: "))
    Equilateral_Triangle = math.sqrt(3)/4 * equil_side**2
    print("Equilateral Triangle: side =", "{:.1f}".format(equil_side), ", area =",(Equilateral_Triangle))
    print("")

    base1 = int(input("Enter base 1: "))
    base2 = int(input("Enter base 2: "))
    height_trapezoid = int(input("Enter height: "))
    Trapezoid = ((base1 + base2)/2) * height_trapezoid 
    print("Trapezoid: base 1 =", "{:.1f}".format(base1), ", base 2 =", "{:.1f}".format(base2), ", height =", "{:.1f}".format(height_trapezoid), ", area =", "{:.1f}".format(Trapezoid))

main()