def function():
    year = int(input("Current Year: "))
    month = int(input("Current Month: "))
    birth_year = int(input("Birth Year: "))
    birth_month = int(input("Birth Month: "))

    ages = (year - birth_year) * 12
    ages = ages +(month - birth_month)

    print("Your age in months: ", ages)

def variable():
    month = int(input("Enter the month: "))
    day = int(input("Enter the day of month: "))

    year = (month - 1) * 30.4 + day
    
    print("The approximate day of the year is: ", year)

def main():
    function()
    variable()
main()


