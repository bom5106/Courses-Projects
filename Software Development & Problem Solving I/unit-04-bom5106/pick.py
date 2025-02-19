import random

def is_correct(guess, answer):
    return guess == answer

def check_guess(guess, answer):
    result = None
    if guess == answer:
        result = 0
    elif guess > answer:
        result = guess - answer
    else:
        result = answer - guess
    return result

def main():
    answer = random.randint(1,10)
    userGuess = int(input('Guess the number between 1-10: '))
    #print(is_correct(userGuess, answer))
    diff = check_guess(userGuess, answer)
    if diff == 0:
        print("You guess correctly!")
    else:
        print("Oooo you are so close, you were only off by:", diff)

if __name__ == '__main__':
    main()