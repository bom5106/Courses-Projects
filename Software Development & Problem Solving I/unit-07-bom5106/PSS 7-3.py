from array_utils import cat_array
from quick_sort import partition
"""
Problem Solving 1
"""
# Insertion_sort
# Best      Average     Worst
# O(n)      O(n^2)      n^2

# Merge Sort
# Best      Average     Worst
# n*log(n)  n*log(n)    n*log(n)

# Quick Sort 
# Best      Average     Worst
# n*log(n)  n*log(n)    n^2

"""
Problem Solving 2
"""
A = [3, 2, 1, 5, 9, 4, 8]
less1, same1, more1 = partition(2, A)
less2, same2, more2 = partition(4, less1)
less_2_same2 = cat_array(less2, same2), 
sorted_less1 = cat_array(less2,same2, more2)
less2, same2, more2 = partition(8, more1)
less2_same2 = cat_array(less2, same2), 
sorted_more1 = cat_array(less2_same2, more2)
sorted_less1_same1 = cat_array(sorted_less1, same1)
sorted_A = cat_array(sorted_less1_same1 , sorted_more1)
print(sorted_A) // [1, 2, 3, 4, 5, 8, 9]


"""
Problem Solving 3
"""
# def quick_sort (an_array):
#    if len (an_array) < 2:
#       return an_array
#    else:
#       pivot = an_array[0]
#       less, same, more = partition (pivot, an_array)
#       new_array = array_cat(quick_sort(less), same)
#       new_array = array_cat (new_array, quick_sort(more))
#       return new_array

# def quick_insertion_sort (an_array, recursions = None):
#     if recursions == None:
#         recursions = 1.7*math.log2(len(an_array)) // it could be C * log(len(an_array)), where 1< C < 3
    
#     if len (an_array) < 2:
#         return an_array 
#     elif recursions < 0:
#         sorts.insertion_sort(an_array)
#         return an_array
#     else:
#         pivot = an_array[0]
#         less, same, more = partition (pivot, an_array)
#         new_array = array_utils.cat_array (quick_insertion_sort(less, recursions-1), same)
#         new_array = array_utils.cat_array (new_array, quick_insertion_sort(more, recursions-1))
#         return new_array