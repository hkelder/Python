import math

print("This program will solve a quadratic equation, as long as you input correct values.")


def quadratics():

    a = float(input("Please give value to A: "))
    b = float(input("Please give value to B: "))
    c = float(input("Please give value to C: "))

    determinant = b * b - (4 * a * c)

    if determinant < 0 or a == 0:
        return ValueError

    elif determinant == 0:
        root = (-b / (2 * a))
        return "Since determinant equals 0, the equations has only 1 root: " + str(root)

    else:
        root1 = (-b + math.sqrt(determinant) / (2 * a))
        root2 = (-b - math.sqrt(determinant) / (2 * a))
        return "Answers are: " + str(root1) + " and " + str(root2)


print(quadratics())
