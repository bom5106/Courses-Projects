#import pick
from pick import *

def test_check_guess_correct():
    # setup
    guess = 5
    answer = 5
    # invoke
    result = check_guess(guess, answer)
    #analyze
    assert result == 0

def test_check_guess_too_low():
    # setup
    guess = 5
    answer = 7
    # invoke
    result = check_guess(guess, answer)
    #analyze
    assert result == 2

def test_check_guess_too_high():
    # setup
    guess = 8
    answer = 5
    # invoke
    result = check_guess(guess, answer)
    #analyze
    assert result == 3