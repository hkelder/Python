

def add(x, y):  # This function adds 2 numbers
    return x + y


def subtract(x, y):  # This function subtracts 2 numbers
    return x - y


def divide(x, y):  # This function divides 2 numbers
    return x / y


def multiply(x, y):  # This function divides 2 numbers
    return x * y


def modulo(x, y):  # This function finds the leftovers of division
    return x % y


def exponent(x, y):
    return x ** y


print("Select operation!\n 1.Add\n 2.Subtract\n 3.Divide\n 4.Multiply\n 5.Modulo\n 6.Exponentiation\n 7.Leave")

choice = input("Enter choice(1,2,3,4,5,6,7): ")  # Asking what function they want to invoke
first_num = int(input("Enter first number: "))  # Asking the first and second number
second_num = int(input("Enter second number: "))

while choice != "7":
    if choice == "1":
        print(first_num, "+", second_num, "=", add(first_num, second_num))

    elif choice == "2":
        print(first_num, "-", second_num, "=", subtract(first_num, second_num))

    elif choice == "3":
        print(first_num, "/", second_num, "=", divide(first_num, second_num))

    elif choice == "4":
        print(first_num, "*", second_num, "=", multiply(first_num, second_num))

    elif choice == "5":
        print(first_num, "%", second_num, "=", modulo(first_num, second_num))

    elif choice == "6":
        print(first_num, "**", second_num, "=", exponent(first_num, second_num))

    else:
        break
