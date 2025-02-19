import random
import merge_sort
import sorts
import time
import array_utils
import array
import arrays
import plotter
import time
import quick_sort

ARRAY_SIZE = 4000
SIZES = array.array("i",[200, 500, 800, 1100, 1400, 1700, 2000])

# def insertion_sort_function_timer(an_array):
#     start = time.perf_counter()
#     sorts.insertion_sort(an_array)
#     stop = time.perf_counter()
#     return stop - start

def sort_function_timer(an_array, sort_function):
    start = time.perf_counter()
    sort_function(an_array)
    stop = time.perf_counter()
    return stop - start

def plot_sort_time_using_random_arrays(sort_function):
    plotter.new_series()
    for i in SIZES:
        an_array = array_utils.random_array(i)
        plotter.add_data_point(sort_function_timer(an_array, sort_function))
    # plotter.plot()

def plot_sort_time_using_sorted_arrays(sort_function):
    plotter.new_series()
    for i in SIZES:
        an_array = array_utils.range_array(1,20)
        plotter.add_data_point(sort_function_timer(an_array, sort_function))
    # plotter.plot()

# Assignment 7.3 Part 6 (Plot Sort Time Using Duplicate Random Arrays)
def plot_sort_time_using_duplicate_random_arrays(size, min, max):
    an_array = arrays.Array(size, 0)
    if max is None:
        max = size / 100
    for index in range(size):
        an_array[index] = random.randint(min, max)
    return an_array

def main():
#    Assignment 7.2
    # plotter.init('Insertion Sort, Insertion Sort w/o swap, and Merge Sort', 'Array Size', 'Time')
    # plot_sort_time_using_random_arrays(sorts.insertion_sort)
    # plot_sort_time_using_random_arrays(sorts.insertion_sort_wo_swap)
    # plot_sort_time_using_random_arrays(merge_sort.merge_sort)
    # plotter.plot()
    # input()

#   Assignment 7.3 Part 1
    plotter.init('Insertion Sort, Merge Sort, Quick Sort', 'Array Size', 'Time')
    plot_sort_time_using_random_arrays(sorts.insertion_sort)
    plot_sort_time_using_random_arrays(merge_sort.merge_sort)
    plot_sort_time_using_random_arrays(quick_sort.quick_sort)
    plotter.plot()
    input("Press Enter to continue...")

    # Which sort algorithm works best?
    # I would say plot_sort_time_using_random_arrays(sorts.insertion_sort) works the best because I tested
    # three of them which the first works fine and other two (merge_sort & quick_sort) were over it which like
    # merge_sort prints first on the graph then quick_sort prints right on top of merge_sort


# # Assignment 7.3 Part 2
    plotter.init('Insertion Sort, Merge Sort, Quick Sort', 'Array Size', 'Time')
    plot_sort_time_using_sorted_arrays(sorts.insertion_sort)
    plot_sort_time_using_sorted_arrays(merge_sort.merge_sort)
    plot_sort_time_using_sorted_arrays(quick_sort.quick_sort)
    plotter.plot()
    input("Press Enter to continue...")

    # What happened and why?
    # When I use the function range_array from array_utils.py. This function works the same way as plot_sort_time_using_random_arrays, except 
    # that it uses sorted arrays. It crash, I knew it would happened because range_array function in plot_sort_time_using_sorted_arrays missing 
    # 1 required positional argument: 'stop'
    # 
    # So, I have fix it the error on line 35 an_array = array_utils.range_array(1,10) to see if it is works but it does not work on SIZES 
    # It does work and see the difference, I see the at quick sort is closer to having everything sorted it becomes slower


# # Assignment 7.3 Part 5
    plotter.init('Insertion Sort, Merge Sort, Quick Insertion Sort', 'Array Size', 'Time')
    plot_sort_time_using_random_arrays(sorts.insertion_sort)
    plot_sort_time_using_random_arrays(merge_sort.merge_sort)
    plot_sort_time_using_random_arrays(quick_sort.quick_insertion_sort)
    plotter.plot()
    input("Press Enter to continue...")
    # Which one works best?
    # I would say Merge Sort is the best because it is on the bottom of the graph which it 
    # is the best and faster

    plotter.init('Insertion Sort, Merge Sort, Quick Insertion Sort', 'Array Size', 'Time')
    plot_sort_time_using_sorted_arrays(sorts.insertion_sort)
    plot_sort_time_using_sorted_arrays(merge_sort.merge_sort)
    plot_sort_time_using_sorted_arrays(quick_sort.quick_insertion_sort)
    plotter.plot()
    input("Press Enter to end the graph...")
    # Comment out the test code and repeat the test using sorted arrays. 
    # Which one works best this time?
    # 
    # Using Sort arraya for insertion, merge, and quick insertion, so i test with sort arrays
    # Insertion Sort works the best this time because of sorted array on insertion sort
    # For Merge and Quick insertion are above the insertion sort


# # Assignment 7.3 Part 6
    print(plot_sort_time_using_duplicate_random_arrays(100, 0, 10))


if __name__ =='__main__':
    main()