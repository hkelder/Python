# Write one line of Python that takes a list
# and makes a new list that has only the even elements of this list in it.

firstList = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

secondList = [num for num in firstList if num % 2 == 0]

print(secondList)
