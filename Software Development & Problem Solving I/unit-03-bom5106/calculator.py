PI = 3.14159

def add(x, y):
    answer = x + y
    return answer

def subtract(x, y):
    answer = x - y
    return answer

def multiply(x, y):
    answer = x * y
    return answer

def divide(x, y):
    answer = x / y
    return answer

def circumference(radius):
    answer = PI * radius * 2
    return answer

def area(radius):
    answer = PI * radius * radius
    return answer

def main():
    x = int(input("Enter x: "))
    y = int(input("Enter y: "))
    print(add(x,y))
    print(subtract(x,y))
    print(multiply(x,y))
    print(divide(x,y))
    print(circumference(5))
    print(area(y))

main()