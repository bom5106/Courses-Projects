from array import array
import arrays
import random

def random_array(size, min_val = 0, max_value = None):
    an_array = arrays.Array(size, 0)
    if max_value is None:
        max_value = size
    for index in range(size):
        an_array[index] = random.randint(min_val, max_value)
    return an_array

def range_array(start, stop, step=1):
    a_range = range(start, stop, step)
    length = len(a_range)
    an_array = arrays.Array(length, 0)
    for index in range(length):
        an_array[index] = a_range[index]
    return an_array

def main():
    random_array(1)
    rand_array = random_array(10)
    print(rand_array)
    rng_array = range_array(2,330,4)
    print(rng_array)

if __name__ == '__main__':
    main()