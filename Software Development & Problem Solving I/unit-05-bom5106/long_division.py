def precise_division(numerator, denominator, precision):
    dec = ""
    whole_number = numerator//denominator
    numerator = numerator - (whole_number*denominator)
    for i in range(precision):
        numerator *= 10
        q = numerator//denominator
        numerator = numerator - (q * denominator)
        dec += str(q)
    return str(whole_number)+'.'+dec


def main():
    command = input("Enter division parameters: ").split(" ")
    num = int(command[0])
    den = int(command[1])
    pre = int(command[2])

    print(precise_division(num, den, pre))

if __name__ == '__main__':
    main()