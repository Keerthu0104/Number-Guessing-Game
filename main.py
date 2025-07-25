import random
import time
import art
from colorama import Fore, Style, init

init(autoreset=True)  # Auto reset colors after each print


def number_guess(user, guess):
    if user == guess:
        return "correct"
    elif user > guess:
        return "too high"
    else:
        return "too low"


def show_progress(attempts_left, total_attempts):
    filled = "🟩" * (total_attempts - attempts_left)
    empty = "⬜" * attempts_left
    print(Fore.YELLOW + f"Progress: {filled}{empty}")


def countdown():
    print(Fore.LIGHTBLUE_EX + "\nGet ready! Game starts in...")
    for i in range(3, 0, -1):
        print(Fore.CYAN + f"⏳ {i}")
        time.sleep(1)
    print(Fore.GREEN + "🎯 Go!\n")


def play_game():
    print(Fore.CYAN + art.logo)
    print(Fore.MAGENTA + "\n🎲 Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")

    print(Fore.LIGHTMAGENTA_EX + "\nChoose a difficulty level:")
    print(Fore.GREEN + "🟢 Easy  💡  ->  10 attempts")
    print(Fore.RED + "🔴 Hard  🔥  ->  5 attempts")

    difficulty_level = input(Fore.CYAN + "\nYour choice: ").lower()
    total_attempts = 10 if difficulty_level == "easy" else 5

    guess_number = random.randint(1, 100)
    attempts_left = total_attempts

    countdown()

    while attempts_left > 0:
        print(Fore.BLUE + f"\nYou have {attempts_left} attempts remaining.")
        show_progress(attempts_left, total_attempts)
        user_input = int(input(Fore.WHITE + "🔢 Make a guess: "))

        output = number_guess(user_input, guess_number)
        print(Fore.LIGHTYELLOW_EX + f"👉 {output}")
        attempts_left -= 1

        if output == "correct":
            print(Fore.GREEN + f"\n🎉 You got it! The answer was {guess_number} ✅")
            break
        elif attempts_left > 0:
            print(Fore.LIGHTBLUE_EX + "🔁 Guess again!")

    if attempts_left == 0 and output != "correct":
        print(Fore.RED + f"\n😢 You've run out of guesses. The number was {guess_number} ❌")


# Main Loop
while True:
    play_game()
    play_again = input(Fore.LIGHTMAGENTA_EX + "\n🔁 Do you want to play again? (yes/no): ").lower()
    if play_again != "yes":
        print(Fore.LIGHTGREEN_EX + "👋 Thanks for playing! Goodbye!")
        break
