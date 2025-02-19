from dataclasses import field
import plotter

def print_lines(filename):
    file = open(filename)
    for line in file: 
        stripped = line.strip()
        print(stripped)

def word_search(filename):
    word = input('Enter a word to search for: ')
    word = word.lower()
    file = open(filename)
    # print(type(file))
    # print(len(file))
    found_it = False
    for line in file:
        file_word = line.strip().lower()
        if word == file_word:
            print('Found the word: ', file_word)
            found_it = True
            break
    file.close()
    if not found_it:
        print('Didn \'t find the word', word)

def longest_word(a_string):
    stripped = a_string.strip()
    longest_word = ''
    if stripped != '':
        words = stripped.split()
        for word in words:
            if len(word) > len(longest_word):
                longest_word = word
    print(longest_word)

def longest_words(filename):
    file = open(filename)
    for line in file:
        longest_word(line)
    file.close()

def print_names(filename):
    with open(filename) as file:
        next(file)
        for line in file:
            fields = line.strip().split(',')
            print(fields[1], fields[0])

def average(filename, column):
    with open(filename) as file:
        header = next(file)
        header_fields = header.strip().split(',')
        col_name = header_fields[column]
        sum = 0
        count = 0
        for line in file:
            fields = line.strip().split(',')
            value = fields[column]
            if value != '':
                sum += float(value)
            count += 1
        print(col_name, 'average: ', (sum / count))

def plot_grades(filename, column):
    with open(filename) as file:
        header = next(file).strip().split(',')
        col_name = header[column]
        plotter.init(('Grades for ' + col_name), 'Students', 'Scores')
        for row in file:
            fields = row.strip().split(',')
            score = float(fields[column])
            plotter.add_data_point(score)
        plotter.plot()

def main():
    # print_lines('Data/alice.txt')
    # word_search('Data/words.txt')
    # longest_word('Data/alice.txt')
    # print_names('data/grades_010.csv')
    # average('data/grades_010.csv', 10)
    plot_grades('data/grades_010.csv', 10)
    input()

if __name__ == '__main__':
    main()