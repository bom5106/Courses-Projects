import arrays
import array_utils
import random
from merge_sort import merge_sort
import sort_times
import sorts
import plotter

def quick_sort(an_array):
    # base case
    if len(an_array) <= 1:
        return an_array
    # recursive case
    else:
        pivot = an_array[0]
        less, same, more = partition(pivot, an_array)
        less_sorted = quick_sort(less)
        more_sorted = quick_sort(more)
        less_same = array_utils.cat_array(less_sorted, same)
        less_same_more = array_utils.cat_array(less_same, more_sorted)
        return less_same_more

def quick_sort_middle(an_array):
    # base case
    if len(an_array) <= 1:
        return an_array
    # recursive case
    else:
        pivot = an_array[len(an_array)//2]
        less, same, more = partition(pivot, an_array)
        less_sorted = quick_sort(less)
        more_sorted = quick_sort(more)
        less_same = array_utils.cat_array(less_sorted, same)
        less_same_more = array_utils.cat_array(less_same, more_sorted)
        return less_same_more

def quick_sort_random(an_array):
    # base case
    if len(an_array) <= 1:
        return an_array
    # recursive case
    else:
        pivot = an_array[random.randint(0, len(an_array)-1)]
        less, same, more = partition(pivot, an_array)
        less_sorted = quick_sort(less)
        more_sorted = quick_sort(more)
        less_same = array_utils.cat_array(less_sorted, same)
        less_same_more = array_utils.cat_array(less_same, more_sorted)
        return less_same_more

def partition(pivot, an_array):
    less = arrays.Array(len(an_array))
    same = arrays.Array(len(an_array))
    more = arrays.Array(len(an_array))
    less_index = 0
    same_index = 0
    more_index = 0
    for i in range(len(an_array)):
        if an_array[i] < pivot:
            less[less_index] = an_array[i]
            less_index += 1
        elif an_array[i] > pivot:
            more[more_index] = an_array[i]
            more_index += 1
        else:
            same[same_index] = an_array[i]
            same_index += 1
    
    return array_utils.copy_array(less, less_index), \
            array_utils.copy_array(same, same_index), \
            array_utils.copy_array(more, more_index)

# Assignment 7.3 Part 4 Create a function named Quick  Insertion Sort
def quick_insertion_sort(an_array):
    # base case
    if len(an_array) < 2:
        return an_array
    # recursive case
    else:
        pivot = an_array[0]
        less, same, more = partition(pivot, an_array)
        less_sorted = quick_sort(less)
        more_sorted = quick_sort(more)
        less_same = array_utils.cat_array(less_sorted, same)
        less_same_more = array_utils.cat_array(less_same, more_sorted)
        return less_same_more

def main():
    # Assignment 7.3 Part 3 (Using plot_sort_time function for quick_sort_mid)
    plotter.init('Insertion Sort, Merge Sort, Quick Sort Middle', 'Array Size', 'Time')
    sort_times.plot_sort_time_using_sorted_arrays(sorts.insertion_sort)
    sort_times.plot_sort_time_using_sorted_arrays(merge_sort)
    sort_times.plot_sort_time_using_sorted_arrays(quick_sort_middle)
    plotter.plot()
    input()
    # Which one works best? What is the time complexity of each sort?
    # When I looked at the graph to see which is the fastest, so the fastest is insertion sort because 
    # it all way to the bottom of the graph and going straight and no up and down. Merge Sort and Quick 
    # Sort Middle are on the top of the graph which both of them are slower

if __name__ =='__main__':
    main()