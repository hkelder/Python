# Generate a random number between 1 and 9 (including 1 and 9).
# Ask the user to guess the number, then tell them whether they guessed too low, too high, or exactly right.
# Extras:
# Keep the game going until the user types “exit”
# Keep track of how many guesses the user has taken, and when the game ends, print this out.
import random


def random_number():
    number = random.randint(1, 9)
    return number


def user_guess():
    print("Please enter a number between 1 and 9:")
    return int(input())


def comparison(randomNumber, userGuess):
    if randomNumber == userGuess:
        return "Well done, you're exactly right!"
    elif randomNumber > userGuess:
        return "Too low."
    elif randomNumber < userGuess:
        return "Too high."


randomNumber = random_number()
userGuess = user_guess()

print(comparison(randomNumber, userGuess))
