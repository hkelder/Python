number = int(input("Please enter a number:"))

if number == 0:
    print("What a conundrum...which one is it now?")

elif number % 2 == 0:
    print("Number", str(number), "is even.")
    print("Boring...")

else:
    print("Number", str(number), "is odd.")
    print("How odd indeed...")

