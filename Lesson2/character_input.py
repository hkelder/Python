# Create a program that asks the user to enter their name and their age.
# Print out a message addressed to them that tells them the year that they will turn 100 years old.
# Extras:
# Add on to the previous program by asking the user for another number and
# printing out that many copies of the previous message.
# Print out that many copies of the previous message on separate lines.

import datetime

name = input("Please enter your name:")
age = int(input("Please enter your age:"))
thisYear = int(datetime.date.today().strftime("%Y"))
old = str((thisYear - age) + 100)

print(name, "you will be 100 years old in year:", old)

messageCopy = int(input("Enter a number: "))

while messageCopy > 0:
    print(name, "you will be 100 years old in year:", old)
    messageCopy = messageCopy - 1

