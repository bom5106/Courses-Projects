from distutils import command
from site import venv

from attr import field
import plotter
def quit():
    quit_or_no = input("Are you sure (y/n): ")
    if quit_or_no == 'y':
        return True
    elif quit_or_no == 'n':
        return False

def plot_grades(filename, firstname, lastname):
    with open(filename) as file:
        header = next(file).strip().split(',')
        plotter.init(('Grades for '+ firstname + ' ' + lastname), 'Grade Item', 'Score' )
        for line in file:
            fields = line.strip().split('"')
            print(fields)
            name = fields[1]
            names = name.strip().split(',')
            lens = len(names)
            if names[0] == lastname and names[lens - 1].strip() == firstname:
                nums = fields[4].strip().split(',')
                for i in range(2, len(nums)):
                    score = float(nums[i])
                    print(score)
                    plotter.add_data_point(score)
                plotter.plot()
                return True




def main():
    while True:
            command_or_quit = input("Enter a command or 'quit' to quit: ")

            if command_or_quit == 'quit':
                result = quit()
                if result == True:
                    print("Goodbye!")
                    break
            try:
                command = command_or_quit.split()
                if command[0] == 'help':
                    print("")
                if command[0] == 'stu':
                    plot_grades(command[1], command[2], command[3])
            except ValueError as venv:
                command = input()
if __name__ == '__main__':
    main()