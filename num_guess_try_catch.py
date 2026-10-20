#!/usr/bin/env python3

# Created By: Sam V
# Date: Oct 13th, 2026
# A number guessing game with crash prevention for non-integer inputs.

import random


def main():
    # Generate a random number between 0 and 9
    random_number = random.randint(0, 9)

    print("Welcome to the Random Number Guessing Game!")
    print("I have selected a number between 0 and 9. Try to guess it!")

    # Get the user's guess as a string
    user_input = input("Enter your guess: ")

    # Try converting the input to an integer to prevent crashes
    try:
        user_guess = int(user_input)

        # Check if the user's guess matches the random number
        if user_guess == random_number:
            print("You Guessed Correctly!")
        else:
            print("You Guessed Wrong. The correct number was:", random_number)

    except ValueError:
        # Executes if the user enters text or decimals instead of an integer
        print(f"{user_input} is not an integer.")


if __name__ == "__main__":
    main()
