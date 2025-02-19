import quick_sort
import array_utils
import time
import sys

sys.setrecursionlimit(5000)

ARRAY_SIZE = 2000

def time_sort(an_array, sort_function):
    start = time.perf_counter()
    sort_function(an_array)
    stop = time.perf_counter()
    return stop - start

def main():
    sorted = array_utils.range_array(0, ARRAY_SIZE)
    rev_sorted = array_utils.range_array(ARRAY_SIZE, -1, -1)
    rand = array_utils.random_array(ARRAY_SIZE)

    print('Quicksort')
    print('  Sorted')
    print(time_sort(sorted, quick_sort.quick_sort))
    print('  Reverse Sorted')
    print(time_sort(rev_sorted, quick_sort.quick_sort))
    print('  Random')
    print(time_sort(rand, quick_sort.quick_sort))
    print()

    print('Quicksort middle')
    print('  Sorted')
    print(time_sort(sorted, quick_sort.quick_sort_middle))
    print('  Reverse Sorted')
    print(time_sort(rev_sorted, quick_sort.quick_sort_middle))
    print('  Random')
    print(time_sort(rand, quick_sort.quick_sort_middle))
    print()

    print('Quicksort random')
    print('  Sorted')
    print(time_sort(sorted, quick_sort.quick_sort_random))
    print('  Reverse Sorted')
    print(time_sort(rev_sorted, quick_sort.quick_sort_random))
    print('  Random')
    print(time_sort(rand, quick_sort.quick_sort_random))

main()