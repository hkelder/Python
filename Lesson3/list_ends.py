# Write a program that takes a list of numbers (for example, a = [5, 10, 15, 20, 25])
# and makes a new list of only the first and last elements of the given list.

import random

firstList = random.sample(range(14), 7)
firstList.sort()
firstLastElementList = []

for element in firstList:
    if element in firstList[:1]:
        firstLastElementList.append(element)
    elif element in firstList[len(firstList) - 1:]:
        firstLastElementList.append(element)

print(firstList)
print(firstLastElementList)
