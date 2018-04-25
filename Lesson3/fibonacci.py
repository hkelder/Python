# Write a program that asks the user how many Fibonacci numbers to generate and then generates them.
# Take this opportunity to think about how you can use functions.
# Make sure to ask the user to enter the number of numbers in the sequence to generate.
# (Hint: The Fibonacci sequence is a sequence of numbers where the next number in the sequence
# is the sum of the previous two numbers in the sequence. The sequence looks like this: 1, 1, 2, 3, 5, 8, 13, …)


def user_input():
    print("Enter the size of the sequence:")
    return int(input())


def sequence(userInput):
    i = 1
    if userInput == 0:
        fibo_list = []
    elif userInput == 1:
        fibo_list = [1]
    elif userInput == 2:
        fibo_list = [1, 1]
    elif userInput > 2:
        fibo_list = [1, 1]
        while i < (userInput - 1):
            fibo_list.append(fibo_list[i] + fibo_list[i - 1])
            i += 1
    return fibo_list


userInput = user_input()

print(sequence(userInput))
