# Write a password generator in Python.
# Be creative with how you generate passwords
# - strong passwords have a mix of lowercase letters, uppercase letters, numbers, and symbols.
# The passwords should be random, generating a new password every time the user asks for a new password.
# Include your run-time code in a main method.
# Extra:
# Ask the user how strong they want their password to be. For weak passwords, pick a word or two from a list.
import random


def password_generation():
    password_characters = "abcdefghijklmnopqrstuvwxyz0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$€&%*()?"
    password_length = random.randint(8, 15)
    password = "".join(random.sample(password_characters, password_length))
    return password


print(password_generation())

