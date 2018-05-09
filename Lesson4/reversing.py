# Write a program (using functions!) that asks the user for a long string containing multiple words.
# Print back to the user the same string, except with the words in backwards order. For example, say I type the string:
#   My name is Michele - Then I would see the string: Michele is name My - shown back to me.


def reversing():
    new_input = input("Please enter a sentence:")
    new_input_split = new_input.split()
    new_input_split.reverse()
    reversed_input = " ".join(new_input_split)
    return reversed_input


print(reversing())
