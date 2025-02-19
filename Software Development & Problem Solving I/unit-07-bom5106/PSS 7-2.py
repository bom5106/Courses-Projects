"""
Problem Solving 1
"""
# Insertion_sort
# Best      Worst
# O(n)      O(n^2)

# Insertion_sort_wo_swap
# Best      Worst
# O(n)      O(n^2)

# Merges_sort 
# Best      Worst
# O(nLog2n) O(nLog2n)

"""
Problem Solving 2
"""
# an_array = arrays.Array(4)
# an_array [0] = 8
# an_array [1] = 4
# an_array [2] = 6
# an_array [3] = 10
# h1, h2 = split(an_array)
# print(h1, ":", h2)                #[8,6] : [4, 10]

# h11, h12 = split(h1)
# h21, h22 = split(h2)
# print(h11, ":", h12, ":", h21,":", h22)       #[8] :  [6] : [4] : [10]

# h1 = merge(h11, h12)
# h2 = merge(h21, h22)
# print(h1, ":", h2)                #[6,8] : [4,10]

# an_array = merge(h1, h2)
# print(an_array)                   #[4, 6, 8, 10]


"""
Problem Solving 3
"""
# an_array = arrays.Array(6)
# an_array [0] = 5
# an_array [1] = 4
# an_array [2] = 6
# an_array [3] = 8
# an_array [4] = 10
# an_array [5] = 1

# h1, h2 = split(an_array)

# h1 = merge_sort(h1)
# print(h1)                 #[5, 6, 10]

# h2 = merge_sort(h2)
# print(h2)                 #[1, 4, 8]

# an_array = merge_sort(h1, h2)
# print(an_array)           #[1, 4, 5, 6, 8, 10]

"""
Problem Solving 4
"""
# def increasing_comparator(a, b):
#     return a <= b

# def decreasing_comparator(a, b):
#       return a >= b

# def shift(an_array, index, comparator=increasing_comparator):
#     while index > 0 and comparator(an_array[index], an_array[index-1]):
#         swap(an_array, index, index-1)
#         index -= 1

# def insertion_sort(an_array, comparator=increasing_comparator):
#     for index in range(1, len(an_array)):
#         shift(an_array, index, comparator)

# def main():
#          an_array = array_utils.random_array(5,0,10);
#          insertion_sort(an_array, decreasing_comparator);
         
# if __name__ == "__main__":
#     main()