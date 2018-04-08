# Write one line of Python that takes a list
# and makes a new list that has only the even elements of this list in it.

# firstList = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

# secondList = [num for num in firstList if num % 2 == 0]

# print(secondList)

import random


def evenList(evenlist):
    evenlist = [num for num in evenlist if num % 2 == 0]
    evenlist.sort()
    return evenlist


def oddList(oddlist):
    oddlist = [num for num in oddlist if num % 2 != 0]
    oddlist.sort()
    return oddlist


numList = []
numList_length = random.randint(5, 15)

while len(numList) < numList_length:
    numList.append(random.randint(1, 75))

numList.sort()

even_list = evenList(numList)
odd_list = oddList(numList)

print("Generated numbers: \n" + str(numList))
print("The odd list is: \n" + str(odd_list))
print("The even list is: \n" + str(even_list))
