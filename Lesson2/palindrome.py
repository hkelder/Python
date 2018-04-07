# Ask the user for a string and print out whether this string is a palindrome or not.


def palindrome():

    userString = input("Enter something:").lower()
    if userString[::-1] == userString:
        print("It's a palindrome")
    else:
        print("This is a normal string.")


palindrome()