# Function that takes an integer and returns the string representation of the roman number


def roman(number):
    symbol = ("M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I")
    value = (1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1)
    roman_num = ""

    for i in range(len(value)):
        count = int(number / value[i])
        roman_num += symbol[i] * count
        number -= value[i] * count
    return roman_num
