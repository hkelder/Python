# Ask the user for a number. Depending on whether the number is even or odd,
# print out an appropriate message to the user.
# Extras:
# If the number is a multiple of 4, print out a different message.
# Ask the user for two numbers: one number to check and one number to divide by.
# If check divides evenly into num, tell that to the user. If not, print a different appropriate message.

number = int(input("Please enter a number:"))

if number == 0:
    print("What a conundrum...which one is it now?")

elif number % 2 == 0:
    print("Number", str(number), "is even.")
    print("Boring...")

else:
    print("Number", str(number), "is odd.")
    print("How odd indeed...")

