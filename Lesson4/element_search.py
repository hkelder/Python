# Write a function that takes an ordered list of numbers
# (a list where the elements are in order from smallest to largest) and another number.
# The function decides whether or not the given number is inside the list and returns an appropriate boolean.
# Extras:
# Use binary search.
import random

print("This program verifies if a number is inside a given list.")


def element_search(ordered_list, element_to_verify):

    for element in ordered_list:
        if element == element_to_verify:
            return True
    return False


if __name__ == "__main__":
    elementList = random.sample(range(20), 10)
    elementList.sort()
    elementToBeVerified = random.randint(0, 35)
    print("The list: " + str(elementList) + " and the number: " + str(elementToBeVerified))
    print(element_search(elementList, elementToBeVerified))

