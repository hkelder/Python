# Create a program that asks the user for a number and then prints out a list of all the divisors of that number. ✓

print("We can currently find the divisions of numbers up to 100.")

num = int(input("Enter a number to divide: "))
numList = range(1, 101)
answerList = []

for element in numList:
    if num % element == 0:
        answerList.append(element)

print(answerList)
