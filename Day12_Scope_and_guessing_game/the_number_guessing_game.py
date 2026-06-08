from number_guessing_art import logo
import random as rd

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5

def get_attempts_for_difficulty(diff: str) -> int:
    return EASY_LEVEL_TURNS if diff == "easy" else HARD_LEVEL_TURNS

def check_guess(guess: int, number: int) -> str:
    if guess < number:
        return "low"
    elif guess > number:
        return "high"
    else:
        return "correct"

def play() -> None:
    print(logo)
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    number = rd.randint(1,100)
    diff_type = input("Choose a difficulty. Type 'easy' or 'hard': ")
    turns = get_attempts_for_difficulty(diff_type)
    while turns:
        print(f"You have {turns} remaining to guess the number.")
        try:
            guess = int(input("Make a guess: "))
            result = check_guess(guess, number)
            if result == "low":
                print("Too low.")
                turns -= 1
            elif result == "high":
                print("Too high.")
                turns -= 1
            else:
                print(f"You got it! The answer was {number}")
                break
        except ValueError:
            print("It is NOT an integer")
        print("Guess again")
    if turns == 0:
        print("You've run out of the guesses, you lose!")
        return

if __name__ == "__main__":
    play()