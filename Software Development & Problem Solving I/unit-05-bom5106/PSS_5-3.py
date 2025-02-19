"""
Problem Solving 1
"""
import csv
def section_avg(filename, section, grade_item):
    with open(filename) as csv_file:
        csv_file_reader = csv.reader(csv_file)
        count = 0
        total = 0
        next(csv_file_reader)
        for record in csv_file_reader:
            if int(record[1]) == section:
                grade = int(record[grade_item])
                total += grade
                count += 1
    return total / count


"""
Problem Solving 2
"""
import csv
# def name_and_address(filename):
#     with open(filename) as csv_file:
#         next(csv_file)
#         for line in csv_file:
#             record = line.split()
#             print(record[0], record[1])
 
def name_and_address(filename):
    with open(filename) as csv_file:
        csv_reader = csv.reader(csv_file)
        next(csv_reader)
        for record in csv_reader:
            print(record[0], record[1])
"""
Problem Solving 3
"""
import re

names = [
    "Tsiatsos, III, Shamella",
    "Myrman, Carlyne",
    "Standeven, Markeith",
    "Adan, IV, Marciano",
    "Pelphrey, Ruven",
    "Schneiderman, Trenee",
    "Hick, Kateland",
    "Blackie, II, Percival",
    "Stueber, Jazzman",
    "Vanderberg, Ileana"
]

def find_matches(regex):
    matches = []
    for name in names:
        if re.findall(regex, name):
            matches += [name]
    print(matches)

find_matches("[tT]")
find_matches("S[a-z]+,.*")
find_matches("P[a-z]+")
first = "Marciano"
last = "Adan"
find_matches(last + ".*" + first)
find_matches(",.*,.*")

"""
Problem Solving 4
"""
def name_and_selection(filename, first, last):
    regex = last + ".*" + first
    with open(filename) as csv_file:
        csv_reader = csv.reader(csv_file)
        next(csv_reader)
        for record in csv_reader:
            if re.findall(regex, record[0]):
                print(record[0], " in Section", record[1])