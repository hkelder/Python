# Generate a random number between 1 and 9 (including 1 and 9).
# Ask the user to guess the number, then tell them whether they guessed too low, too high, or exactly right.
# Extras:
# Keep the game going until the user types “exit”
# Keep track of how many guesses the user has taken, and when the game ends, print this out.
import random


def guessing_game():
    randomNumber = random.randint(1, 9)
    userGuess = 0
    count = 0

    while userGuess != "exit" and int(userGuess) != randomNumber:
        userGuess = input("Guess a number between 1 and 9 or type exit.").lower()
        if userGuess == "exit":
            break

        userGuess = int(userGuess)

        if userGuess < 1 or userGuess > 9:
            print("Invalid number, try again!")
            continue
        elif userGuess < randomNumber:
            print("Too low, try again!")
            count += 1
            continue
        elif userGuess > randomNumber:
            print("Too high, try again!")
            count += 1
            continue
        elif userGuess == randomNumber:
            count += 1
            print("You got it! It took you", count, "tries.")


guessing_game()
