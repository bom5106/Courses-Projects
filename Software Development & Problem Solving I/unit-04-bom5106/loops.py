from cgitb import reset
from lib2to3.pgen2 import token


def countdown(number):
    sum = 0
    while number >=0:
        sum += number
        print(number)
        number -= 1
        print('Sum = ', sum)

def countup(number):
    sum = 0
    current = 0
    while current <= number:
        sum += current
        print(current)
        current += 1
    print('Sum = ', sum)

def print_chars(a_string):
    print(a_string)
    index = 0
    while index < len(a_string):
        print(a_string[index])
        index +=1

def print_chars_reverse(a_string):
    print(a_string)
    index =-1
    while index >= len(a_string):
        print(a_string[index])
        index -=1

def prompt_until_zero():
    sum = 0
    while True:
        number = int(input('Enter a number: '))
        if number == 0:
            break
        elif number % 2 == 0:
            continue
        else:
            sum += number
    print('Sum = ', sum)

#Problem Solving 3
def palindrome(a_string):
    i = 0
    j = len(a_string) - 1
    result = True
    while i < j:
        if a_string[i] !=a_string[j]:
            result = False
            break
        i += 1
        j -= 1
    return result

def print_range(a_range):
    index = 0
    while index < len(a_range):
        print(a_range[index], end = ' ')
        index += 1
    print()

def print_range_for(a_range):
    for ele in a_range:
        print(ele, end = ' ')
    print()

def reverse_string(a_string):
    result = ''
    for letter in a_string:
        result = letter + result

    # for index in range(len(a_string))
    # result = a_string[index] + result
    return result

def split_string(a_string, delim = ' '):
    tokens = a_string.split(delim)
    # print(type(tokens))
    for token in tokens:
        print(token)

def main():
    # countdown(5)
    # countup(7)
    # print_chars('Hello World!')
    # print_chars_reverse('Backwards')
    # prompt_until_zero()

    # print(palindrome('abcba'))
    # print(palindrome('abccba'))
    # print(palindrome('Hello World!'))

    # print_range(range(11))
    # print_range(range(0,21,2))
    # print_range(range(5,16,2))
    # print_range(range(10,-1,-1))

    # print_range_for(range(11))
    # print_range_for(range(0,21,2))
    # print_range_for(range(5,16,2))
    # print_range_for(range(10,-1,-1))

    # print(reverse_string("Brandon Mata"))

    split_string('This is a test')
main()