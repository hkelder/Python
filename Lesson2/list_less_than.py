# 1) Take a list, say for example this one:
# a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# and write a program that prints out all the elements of the list that are less than 5.✓
# Extras:
# 2) Instead of printing the elements one by one,
# make a new list that has all the elements less than 5 from this list in it and print out this new list.✓
# Write this in one line of Python.
# 3) Ask the user for a number and
# return a list that contains only elements from the original
# list a that are smaller than that number given by the user ✓
print("This program will list all numbers smaller than your input from a list of prime numbers up to 27.")

primes = [1, 2, 3, 5, 7, 11, 13, 17, 19, 27]
lessThanUserInput = []
userInput = int(input("Enter a number: "))

for integerInPrimes in primes:
    if integerInPrimes < userInput:
        lessThanUserInput.append(integerInPrimes)

print(lessThanUserInput)
