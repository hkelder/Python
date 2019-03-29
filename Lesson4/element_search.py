# Write a function that takes an ordered list of numbers
# (a list where the elements are in order from smallest to largest) and another number.
# The function decides whether or not the given number is inside the list and returns an appropriate boolean.
# Extras:
# Use binary search.
import random

print("This program verifies if a number is inside a given list.")


def element_search(ordered_list, element_to_verify):
    start_index = 0
    end_index = len(ordered_list) - 1

    while True:
        middle_index = int((end_index + start_index) / 2)

        if middle_index == start_index or middle_index == end_index:
            if ordered_list[middle_index] == element_to_verify or ordered_list[end_index] == element_to_verify:
                return True
            else:
                return False

        middle_element = ordered_list[middle_index]
        if middle_element == element_to_verify:
            return True
        elif middle_element > element_to_verify:
            end_index = middle_index
        else:
            start_index = middle_index


if __name__ == "__main__":
    elementList = random.sample(range(20), 10)
    elementList.sort()
    elementToBeVerified = random.randint(0, 35)
    print("The list: " + str(elementList) + " and the number: " + str(elementToBeVerified))
    print(element_search(elementList, elementToBeVerified))

