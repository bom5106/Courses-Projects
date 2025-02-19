from array import array
import array_utils
import arrays
def swap(an_array,a,b):
    temp = an_array[a]
    an_array[a] = an_array[b]
    an_array[b] = temp

def shift(an_array,index):
    while index > 0 and an_array[index] < an_array[index - 1]:
        swap(an_array,index,index-1)
        index -= 1

def insertion_sort(an_array):
    for index in range(1, len(an_array)):
        shift(an_array, index)

def insertion_sort_backwards(an_array):
    for index in range(len(an_array)-1, -1, -1):
        shift_backwards(an_array,index)
        print(an_array)

def shift_backwards(an_array, index):
    while index < len(an_array)-1 and an_array[index+1] < an_array[index]:
        swap(an_array, index, index+1)
        index += 1

def shift_wo_swap(an_array, index):
    target = an_array[index]
    target_index = index
    while target_index > 0 and target < an_array[target_index-1]:
        an_array[target_index] = an_array[target_index-1]
        target_index -= 1
    an_array[target_index] = target

def insertion_sort_wo_swap(an_array):
    for index in range(1, len(an_array)):
        shift_wo_swap(an_array, index)

def main():
    # an_array = array_utils.range_array(0,10)
    # an_array = array_utils.random_array(10)
    # print(an_array)
    # swap(an_array,0,1)
    #swap(an_array,1,2)
    # print(an_array)
    # shift(an_array, 2)
    # insertion_sort(an_array)
    # print(an_array)

    an_array = arrays.Array(5)
    an_array[0] = 5
    an_array[1] = 3
    an_array[2] = 7
    an_array[3] = 4
    an_array[4] = 1
    insertion_sort_backwards(an_array)
    print(an_array)

if __name__ =='__main__':
    main()