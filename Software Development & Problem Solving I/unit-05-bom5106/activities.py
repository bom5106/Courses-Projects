from unittest import result


def numbers():
    total_sum = 0
    while True:
        filename = input('Enter a file to sum: ')
        if filename == '':
            break
        try:
            with open(filename) as file:
                sum = 0
                for number in file:
                    try:
                        sum += int(number.strip())
                    except ValueError:
                        print('Non Numeric Data: ', number)
                print('Sum for file: ', filename, 'is: ', sum)
                total_sum += sum
        except FileNotFoundError:
            print('File does not exist ', filename)
    
    print('Total sum: ', total_sum)

def division():
    errors = 0
    while True:
        numerator = input('Enter Numerator: ')
        denominator = input('Enter Deminator: ')
        if numerator == '' or denominator == '':
            break
        try:
            numerator = float(numerator)
            denominator = float(denominator)
            result = numerator / denominator
            print(numerator, ' / ', denominator , ' = ', result)
        except ValueError as ve:
            errors += 1
            if errors >= 3:
                raise ve
            print('Non numeric data, you have ', errors, 'serrors')
        except ArithmeticError:
            errors += 1
            if errors >= 3:
                raise ve
            print('Denominator cannot be 0, you have ', errors, 'serrors')

def password():
    password = input('Enter a new password: ')
    length = len(password)
    if length < 10 or length > 20:
        raise ValueError('Password must be between 10 and 20 character')
    confirm = input('Confirm new Password: ')
    if password != confirm:
        raise ValueError('Password do not match')
    return password

def exponent(base, power):
    result = 1
    if power < 0:
        raise ValueError
    for _ in range(power):
        result = result * base
    return result

def main():
    # numbers()
    # division()
    try:
        password()
    except Exception as e:
        print(e)

if __name__ == '__main__':
    main()