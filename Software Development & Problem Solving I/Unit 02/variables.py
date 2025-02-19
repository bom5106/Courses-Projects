def variable_practice():
    age_in_month = 54 * 12 + 8
    days_in_year = 365
    first_pet = "Molly"
    pi = 3.1415

    print(age_in_month, type(age_in_month))
    print(days_in_year, type(days_in_year))
    print(first_pet, type(first_pet))
    print(pi, type(pi))

def expressions_practice():
    a_const = 123.456
    addition = 4+5
    exponent = 5 ** 6
    floor_division = 10 // 3
    mod = 10 % 3
    parens = (4 + 5) * 8
    mix_it_up = (4 + 5) * 6 // (5 - 3)

    print(a_const, type(a_const))
    print(addition, type(addition))
    print(exponent, type(exponent))
    print(floor_division, type(floor_division))
    print(mod, type(mod))
    print(parens, type(parens))
    print(mix_it_up, type(mix_it_up))

def prompt_and_print():
    val_1 = int(input('Enter a number: '))
    val_2 = int(input('Enter a number: '))

    print(val_1 + val_2)
    print(val_1 - val_2)
    print(val_1 * val_2)
    print(val_1 / val_2)


def main():
    variable_practice()
    print()
    expressions_practice()
    print()
    prompt_and_print()
main()