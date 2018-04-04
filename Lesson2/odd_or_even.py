# Ask the user for a number. ✓
# Depending on whether the number is even or odd,
# print out an appropriate message to the user. ✓
# Extras:
# If the number is a multiple of 4, print out a different message. ✓
# Ask the user for two numbers: one number to check and one number to divide by. ✓
# If check divides evenly into num, tell that to the user. If not, print a different appropriate message. ✓

number = int(input("Please enter a number:"))

if number == 0:
    print("What a conundrum...which one is it now?")

elif number % 4 == 0:
    print("Number", str(number), "is a multiple of 4 and is even.")

elif number % 2 == 0:
    print("Number", str(number), "is even.")
    print("Boring...")

else:
    print("Number", str(number), "is odd.")
    print("How odd indeed...")

num = int(input("Enter a number you want checked:"))
check = int(input("Enter the number you want to check with:"))

if num % check == 0:
    print("Those 2 numbers divide evenly.")
else:
    print("Those 2 numbers do not divide evenly.")
