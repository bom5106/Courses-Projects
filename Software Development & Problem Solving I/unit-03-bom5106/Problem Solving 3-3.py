"""
Problem 1
"""
#answer = square_area(8)
#assert answer == 64'

#answer = square_area(8)
#assert answer < 64

#answer = square_area(8)
#assert answer > 64

#Problem 1: Reasonable test cases:
#Guess is less than 1
#Guess is greater than 10
#Guess is too low (less than answer)
#Guess is too high (Greater than answer)
#Guess is correct

"""
Problem 2 & Problem 3
"""
MIN = 1
MAX = 10
OUT_OF_RANGE = "Out of Range"
TOO_LOW = "Too Low!"
TOO_HIGH = "Too High!"
CORRECT = "CORRECT!"
GAME_OVER = "GAME OVER"


def testing_check_guess_range_low():
    answer = 5
    guess = MIN-1
    result = check_guess(answer,guess)
    assert result == OUT_OF_RANGE

def testing_check_guess_range_high():
    answer = 5
    guess = MAX+1
    result = check_guess(answer,guess)
    assert result == OUT_OF_RANGE
    
def check_guess(answer, guess):
    return

"""
Problem 4
"""
#1. Generate random number between 1 to 10
#2. Ask user for guess
#3. Call check guess function and print response
#4. If guess is not correct repeat 2 and 3
#5. If guess is not correct repeat 2 and 3
#6. If guess is not correct repeat 2 and 3
#7. Game Over!