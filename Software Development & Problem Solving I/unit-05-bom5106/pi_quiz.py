from attr import field

pi = '3.1415926535897932384626433832795028841971693993751058209749445923078164062862089986280348253421170679'
pi_decimals = str(pi.split(".")[1::][0])

def pi_tester():
    counter = 0
    for answer in pi_decimals:
        val2 = input('Enter the number: ')
        if val2 == answer:
            print('That is correct!')
            counter += 1
        if val2 != answer:
            print('That is wrong, the answer is', answer)
    print('Number of Correct Guess: ', counter)
    return counter

def display_score(score):
    
    if score > 0 and score < 4:
        print('PI Neophyte')
    elif score > 5 and score < 9:   
        print('PI Novice')
    elif score > 10 and score < 24:
        print('PI Journeyman')
    elif score > 25 and score < 49:
        print('PI Enthusiast')
    elif score > 50 and score < 96:
        print('PI Connoisseur')
    elif score > 97 and score < 100:
        print('PI Expert')
    elif score == 100:
        print('PI Imposter')
    
def main():
    score = pi_tester()
    display_score(score)

if __name__ == '__main__':
    main()