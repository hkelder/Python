# Take two lists, say for example these two:
# a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
# Write a program that returns a list that contains only the elements that are common between the lists(no dupes).
# Make sure your program works on two lists of different sizes.
# Write this using at least one list comprehension.
# Extra:
# Randomly generate two lists to test this

import random

firstList = random.sample(range(30), 15)
secondList = random.sample(range(40), 20)
commonList = [element for element in firstList if element in secondList]
commonList.sort()


print("Common elements between 2 lists: " + str(commonList))
