# Write a function that takes an ordered list of numbers
# (a list where the elements are in order from smallest to largest) and another number.
# The function decides whether or not the given number is inside the list and returns an appropriate boolean.
# Extras:
# Use binary search.
import random


def element_search():
    print("This program verifies if a number is inside a given list.")

    elementList = random.sample(range(20), 10)
    elementToBeVerified = random.randint(0, 100)

    elementList.sort()

    if str(elementToBeVerified) in str(elementList):
        print("Number " + str(elementToBeVerified) + " is inside the list.")
        print("The list elements are: " + str(elementList))
    else:
        print("Number " + str(elementToBeVerified) + " isn't inside the list.")
        print("The list elements are: " + str(elementList))


element_search()
