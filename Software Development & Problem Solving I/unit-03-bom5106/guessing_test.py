import random

MIN = 1
MAX = 10
OUT_OF_RANGE = "Guess out of Range!"
TOO_LOW = "Too Low!"
TOO_HIGH = "Too High!"
CORRECT = "CORRECT!"
GAME_OVER = "GAME OVER!"

def check_guess(guess, answer):
    if guess > answer:
        print(TOO_HIGH)
    if guess < answer:
        print(TOO_LOW)
    if guess == answer:
        print(CORRECT)
        return True
    if guess > MAX and guess < MIN:
        print(OUT_OF_RANGE)
    return False
    

def testing_check_guess_range_low():
    result = check_guess()
    assert result == OUT_OF_RANGE

def testing_check_guess_range_high():
    result = check_guess()
    assert result == OUT_OF_RANGE
    
   
def main():
    answer = random.randint(MIN, MAX)
    guess = int(input("Enter guess: "))
    if not check_guess(guess,answer):
        guess = int(input("Enter guess: "))
        if not check_guess(guess,answer):
            guess = int(input("Enter guess: "))
            if not check_guess(guess,answer):
                print("The answer is ",answer)
    print(GAME_OVER)

main()