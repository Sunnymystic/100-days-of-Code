from number_guessing_art import logo
import random as rd

def get_attempts_for_difficulty(diff: str) -> int:
    return 10 if diff == "easy" else 5

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
    attempts = get_attempts_for_difficulty(diff_type)
    while attempts:
        print(f"You have {attempts} remaining to guess the number.")
        try:
            guess = int(input("Make a guess: "))
            result = check_guess(guess, number)
            if result == "low":
                print("Too low.")
                attempts -= 1
            elif result == "high":
                print("Too high.")
                attempts -= 1
            else:
                print(f"You got it! The answer was {number}")
                break
        except ValueError:
            print("It is NOT an integer")
        print("Guess again")


if __name__ == "__main__":
    play()