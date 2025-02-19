"""Problem Solving 1"""
from attr import fields


def crazy_output():
  x = input("Type something: ")
  try:
    int_x = int(x)
    print("You entered an integer:", int_x)
  except ValueError:
    try:
      float_x = float(x)
      print("You entered a float:", float_x)
    except:
      print("The third character is:", x[2])


"""
1.) 1 -> You entered an integer: 1
2.) 12.34 -> You entered a float: 12.34
3.) abc -> The third character is: c
4.) -1 -> You entered an integer: -1
5.) ab -> Index Error
"""

"""
Problem Solving 2
"""
def count_words(filename):
    with open(filename) as file:
        word = 0
        for line in file:
            line = line.strip()
            line_words = line.split()
            words += len(line_words)
        return words

"""
Problem Solving 3
"""
def lab_average(csv_file, first_name, last_name):
    with open(csv_file) as file:
        for line in file:
            fields = line.strip().split(",")
            if fields[0] == last_name and fields[1] == first_name:
                sum = 0
                for i in range(2,11):
                    sum += float(fields[0])
                return sum/8
    
    raise ValueError ("Could not find " + first_name + " " + last_name)

"""
Problem Solving 4
"""
def open_file():
    while True:
        try:
            filename = input("Enter the filename: ")
            file = open(filename)
            return file
        except FileNotFoundError:
            print("File does not exist. Try Again.")

# def main():
#     # crazy_output()

# if __name__ == '__main__':
#     main()