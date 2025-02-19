import plotter
import time
import arrays
from searches import binary_search
from array_utils import range_array

def average_binary_search(size, runs):
    a_range = range(size)
    print(a_range)
    length = len(a_range)
    an_array = arrays.Array(length,0)
    for index in range(length):
        an_array[index] = a_range[index]
    
    step = len(an_array) // runs

    execution_time = 0.0
    counter = 0
    for index in range(len(an_array), step):
        start_time = time.time()
        binary_search(an_array, an_array[index])
        execution_time += time.time()-start_time
        counter+=1
    average_time = execution_time/counter
    return average_time



def plot_average_binary_searches(min_size, max_size, runs):
   plotter.init('Binary Search', 'Length', 'Time')
   for index in range(min_size, max_size):
        average_binary_search(index,runs)
   plotter.plot

        

def main():
    # average_binary_search(100, 10)
    plot_average_binary_searches(10, 1000, 25)

if __name__ == '__main__':
    main()