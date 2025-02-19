import arrays
import array_utils
import random
import time
import searches
import math
import turtle

REALLY_BIG_NUMBER = 1000000

def making_arrays():
    array1 = arrays.Array(5)
    print(array1)
    array2 = arrays.Array(1,0)
    print(array2)
    array3 = arrays.Array(10, '')
    print(array3)
    array4 = arrays.Array(20, False)
    print(array4)

def while_fill(an_array):
    index = 0
    length = len(an_array)
    while index < length - 2:
        an_array[index] = index
        index += 1

def for_fill(an_array):
    for index in range(1, len(an_array)-1):
        an_array[index] = index

def roll_the_die(sides):
    roll = random.randint(1, sides)
    return roll    

def linear_search_timer(an_array, target):
    start = time.perf_counter()
    searches.linear_search(an_array, target)
    stop = time.perf_counter()
    return stop - start

def binary_search_timer(an_array, target):
    start = time.perf_counter()
    searches.binary_search(an_array, target)
    stop = time.perf_counter()
    return stop - start

def time_linear():
    an_array = array_utils.range_array(1, REALLY_BIG_NUMBER)
    # an_array = array_utils.random_array(REALLY_BIG_NUMBER)
    length = len(an_array)
    first = an_array[0]
    middle = an_array[length//2]
    last = an_array[length-1]

    print(linear_search_timer(an_array, first))
    print(linear_search_timer(an_array, middle))
    print(linear_search_timer(an_array, last))

def time_binary():
    an_array = array_utils.range_array(1, REALLY_BIG_NUMBER)
    # an_array = array_utils.random_array(REALLY_BIG_NUMBER)
    length = len(an_array)
    first = an_array[0]
    middle = an_array[length//2]
    last = an_array[length-1]

    print(binary_search_timer(an_array, first))
    print(binary_search_timer(an_array, middle))
    print(binary_search_timer(an_array, last))

def print_odds(an_array):
    for index in range(len(an_array)):
        if an_array[index] % 2 == 1:
            print(an_array[index], end = ' ')
    print()

def print_odds_rec(an_array, index=0):
    # base case . . . get me out of here when I'm done
    if index >= len(an_array):
        print()
    # recursive case
    else:
        # do some work
        if an_array[index] % 2 == 1:
            print(an_array[index], end = ' ')
        #  call myself
        print_odds_rec(an_array, index + 1)

def countdown(n):
    if n < 0:
        result = None
    elif n == 0:
        print(n)
        result = 0
    else:
        print(n, end= ' ')
        result = n + countdown(n - 1)
        # print(n, end= ' ')
    return result

def count_up(number):
    if number == 0:
        print(number)
    else:
        count_up(number - 1) #recursion
        print(number) #Do work

def factorial(n):
    if n < 0:
        result = None
    elif n == 0 or n == 1:
        result = 1
    else:
        result = n * factorial(n - 1)
    return result    

def circles(radius, depth):
    if depth == 0:
        return 0
    elif depth == 1:
        turtle.circle(radius)
        return math.pi * radius * 2
    else:
        total = math.pi * radius * 2
        for _ in range(4):
            turtle.circle(radius, 90)
            total += circles(radius/2, depth-1)
        return total

def main():
    # # making_arrays()
    #  a= arrays.Array(10,'Hello')
    #  print(a)
    #  for_fill(a)
    #  print(a)
    random.seed(1)
    # for _ in range(10):
    #     print(roll_the_die(6))
    print("Time Linear")
    time_linear()
    print("Time Binary")
    time_binary()
    # an_array = array_utils.range_array(0,101)
    # print_odds_rec(an_array)
    # print(countdown(10))
    # print(factorial(10))
    # turtle.speed(0)
    # turtle.penup()
    # turtle.tracer(False)
    # turtle.setpos(0,-200)
    # turtle.pendown()
    # print(circles(200,5))
    # turtle.tracer(True)
    # input()
    # count_up(10)


if __name__ == '__main__':
    main()