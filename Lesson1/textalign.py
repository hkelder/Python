print("Please make sure that the width is at least 10, for a pleasant table.")
width = int(input("Enter the width:"))
if width < 10:
    raise ValueError('Please enter a number bigger or equal to 10')


with open(r'.\info.txt', 'r') as info:
    for line in info:
        data = line.split()
        print('{0[0]:>{width}}{0[1]:>{width}}{0[2]:>12}'.format(data, width=width))
