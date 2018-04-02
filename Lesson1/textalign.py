print("Please make sure that the width is at least 11, for a pleasant table.")
width = int(input("Enter the width:"))
with open(r'C:\Users\henri\Desktop\Python\Lesson1\info.txt', 'r') as info:
    for line in info:
        data = line.split()
        print('{0[0]:>{width}}{0[1]:>{width}}{0[2]:>12}'.format(data, width=width))
