# Function which takes string as an input and turns it into "correctly" capitalized string.
# Meaning that in every word in the string must be capitalized.


def capitalizing_this(input_string):
    b = []
    for temp in input_string.split(' '):
        b.append(temp.capitalize())
    return ' '.join(b)