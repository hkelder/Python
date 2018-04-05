# Write a program that returns a list that contains only the elements that are common between the lists (no dupes).
# Make sure your program works on two lists of different sizes.
# Extra:
# Randomly generate two lists to test this.
import random

a = range(1, random.randint(1, 30))
b = range(1, random.randint(1, 75))
c = []

for num in a:
    if num in b:
        c.append(num)

print(c)
