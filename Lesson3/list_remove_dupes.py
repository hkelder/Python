# Write a program (function!) that takes a list and returns a new list that contains
# all the elements of the first list minus all the duplicates.
# Extras:
# Write two different functions to do this - one using a loop and constructing a list, and another using sets.
# Go back and do Exercise 5 (list_overlap) using sets, and write the solution for that in a different function.
import random

list_a = range(1, random.randint(1, 20))


def sorting_with_loop(list_a):
    list_b = []
    for element in list_a:
        if element not in list_b:
            list_b.append(element)
    return list_b


def sorting_with_set(list_a):
    return list(set(list_a))


print(sorting_with_loop(list_a))
print(sorting_with_set(list_a))



