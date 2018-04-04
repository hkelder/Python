import datetime

name = input("Please enter your name:")
age = int(input("Please enter your age:"))
thisYear = int(datetime.date.today().strftime("%Y"))
old = str((thisYear - age) + 100)

print(name, "you will be 100 years old in year:", old)

messageCopy = int(input("Enter a number: "))

while messageCopy > 0:
    print(name, "you will be 100 years old in year:", old)
    messageCopy = messageCopy - 1

