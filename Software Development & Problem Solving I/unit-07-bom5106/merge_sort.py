import arrays
import array_utils

def merge_sort(an_array):
    pass

def split(an_array):
    evens_count = (len(an_array) + 1) // 2
    odds_count = len(an_array) // 2
    half1 = arrays.Array(evens_count)
    half2 = arrays.Array(odds_count)

    isEven = True
    for i in range(len(an_array)):
        if isEven:
            half1[i // 2] = an_array[i]
        else:
            half2[i // 2] = an_array[i]
        isEven = not isEven

    return half1, half2

def merge(half1, half2):
    result = arrays.Array(len(half1) + len(half2))
    i1 = 0
    i2 = 0
    while i1 < len(half1) and i2 < len(half2):
        if half1[i1] <= half2[i2]:
            result[i1 + i2] = half1[i1]
            i1 += 1
        else:
            result[i1 + i2] = half2[i2]
            i2 += 1
    if i1 < len(half1):
        for i in range(i1, len(half1)):
            result[i + i2] = half1[i]
    elif i2 < len(half2):
        for i in range(i2, len(half2)):
            result[i + i1] = half2[i]
    return result

def merge_sort(an_array):
    # Base Case
    if len(an_array) <= 1:
        return an_array
    # recursive case
    else:
        (h1, h2) = split(an_array)
        result = merge(merge_sort(h1), merge_sort(h2))
        return result

def swap(an_array,a,b):
    temp = an_array[a]
    an_array[a] = an_array[b]
    an_array[b] = temp

#array1 - sorted
#array2 - reverse sorted
def swap_merge(array1, array2):
    for index in range(len(array2)//2):
        swap(array2, index, len(array2)-1-index)
    return merge(array1, array2)

#you know what is array_utils.range_array?
def main():
    array1 = array_utils.range_array(0, 5)
    array2 = array_utils.range_array(3, -5, -1)
    swap_merge(array1, array2)
    print(swap_merge)

if __name__ =='__main__':
    main()