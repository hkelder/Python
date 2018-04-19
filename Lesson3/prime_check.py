# One of the tools programming gives us is the ability to break down problems into easie or reusable subproblems.
# It is good practice to have a function have a single purpose,
#  and the name of that function should hint at it’s purpose in some way.


def user_input():
    print("Please enter a number:")
    return int(input())


def prime_cheker(userInput):
    if userInput / 1 and userInput / userInput == 1:
        return "This is a prime number"
    else:
        return "This isn't a prime number"


userInput = user_input()

print(prime_cheker(userInput))
