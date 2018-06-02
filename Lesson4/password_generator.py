# Write a password generator in Python.
# Be creative with how you generate passwords
# - strong passwords have a mix of lowercase letters, uppercase letters, numbers, and symbols.
# The passwords should be random, generating a new password every time the user asks for a new password.
# Include your run-time code in a main method.
# Extra:
# Ask the user how strong they want their password to be. For weak passwords, pick a word or two from a list.
import random

WEAK_PASSWORD_LIST = ["123456789", "password", "987654321", "weakpassword", "choosestrong", "myfeetsmell"]


def password_generation():
    password_characters = "abcdefghijklmnopqrstuvwxyz0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$€&%*()?"
    password_length = random.randint(8, 15)
    password = "".join(random.sample(password_characters, password_length))
    return password


def user_choice():
    while True:
        choice = input("Do you want a strong or a weak password?").lower()
        if choice in ["strong", "weak"]:
            return choice
        else:
            print("Please enter one of the following: strong, weak")


def user_password(userChoice, passwordGeneration):
    if userChoice == "strong":
        return passwordGeneration
    elif userChoice == "weak":
        return random.choice(WEAK_PASSWORD_LIST)


userChoice = user_choice()
passwordGeneration = password_generation()

print(user_password(userChoice, passwordGeneration))
