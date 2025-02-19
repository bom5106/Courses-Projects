import csv
import re

def opener(filename):
    result = False
    try:
        with open(filename) as file:
            result = True
    except FileNotFoundError as e:
        print(e)
    return result

def names_and_addresses(filename):
    try:
        with open(filename) as csv_file:
            csv_reader = csv.reader(csv_file)
            next(csv_reader)
            for row in csv_file:
                # fields = row.strip().split(',')
                print('name', row[0], 'address', row[1])
    except FileNotFoundError as e:
        print(e)

def averages(filename, column):
    try:
        with open(filename) as csv_file:
            csv_reader = csv.reader(csv_file)
            next(csv_reader)
            sum = 0
            count = 0
            for row in csv_reader:
                # print('name', row[0], 'addess', row[1])
                try:
                    sum += float(row[column])
                except ValueError as e:
                    print(e)
                except IndexError as e:
                    print(e)
                count +=1
            average = sum / count
            return round(average,2)
    except FileNotFoundError as e:
        print(e)    

def zip_check(filename):
    zips = '[789]\d{4}'
    with open(filename) as csv_file:
        csv_reader = csv.reader(csv_file)
        next(csv_reader)
        for record in csv_reader:
            address = record[1]
            if re.findall(zips, address):
                print(record[0], address)

def main():
    # filename = input('Enter a filename: ')
    # names_and_addresses(filename)
    # print(averages('data/full_grades_010.csv', 100))
    zip_check('data/full_grades_010.csv')

if __name__ == '__main__':
    main()