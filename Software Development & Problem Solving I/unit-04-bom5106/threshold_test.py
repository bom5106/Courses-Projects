import random

def within_threshold(a,b, threshold):
    return a + b == threshold

def check_guess(a,b, threshold):
    result = None
    if a+b == threshold:
        result = 0
    elif a+b > threshold:
        result = a+b - threshold
    else:
        result = threshold - a+b
    return result

def test_check_guess_correct():
    a = 5
    b = 5
    threshold = 5
    result = check_guess(a,b, threshold)
    assert result == 0

def test_check_guess_too_low():
    a = 9
    b = 6
    threshold = 7
    result = check_guess(a,b, threshold)
    assert result == 2

def test_check_guess_too_high():
    a = 10
    b = 9
    threshold = 5
    result = check_guess(a,b, threshold)
    assert result == 3

def main():
    threshold = random.randint(1,10)
    userGuess = int(input('Guess the number between 1-10: '))
    diff = check_guess(userGuess, threshold)
    if diff == 0:
        print("Correctly!")
    else:
        print("Sorry, You were only off by:", diff)

if __name__ == '__main__':
    main()