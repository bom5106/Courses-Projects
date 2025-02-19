import arrays as ar
import array_utils

def linear_recursive(arr, i ,target):
    if (arr[i] == target):
        return i
    elif (i == len(arr) - 1):
        return None
    else:
        return linear_recursive(arr, i + 1, target)

def count_vowels(s, index):
    if index == len(s):
        return 0
    if s[index] == 'e' or s[index]=='a' or s[index] == 'i' or s[index] == 'o' or s[index] == 'u':
        return count_vowels(s, index + 1) + 1
    return count_vowels(s, index+1)

def main():
    a = count_vowels("Code Commentary is useful", 0)
    print(a)

if __name__ =='__main__':
    a = ar.Array(5, 0)
    res = linear_recursive(a,0,4)
    print(res)
    a[3] = 4
    res = linear_recursive(a,0,4)
    print(res)

    main()