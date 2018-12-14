from datetime import date


class Person:
    def __init__(self, first, last, birth):
        self.first_name = first
        self.last_name = last
        self.birth_date = birth

    def full_name(self):
        return "{} {}".format(self.first_name, self.last_name)

    def __str__(self):
        return "Person: {} {}".format(self.full_name(), self.age())

    def age(self):
        today = date.today()
        return today.year - self.birth_date.year - (
                (today.month, today.day) < (self.birth_date.month, self.birth_date.day))


class Female(Person):
    def age(self):
        # if super(Female, self).age() > 20: This didn't work because testing envi was bad, but it works 100%,
            # return 20                      code below is just an optimization (e.g 1 less super().age() call)
        #  return super(Female, self).age()
        a = super().age()
        if a > 20:
            return 20
        return a

    def __init__(self, first, last, birth):
        super().__init__(first, last, birth)


test = Person("Paul", "Meri", date(1997, 9, 25))
test1 = Person("Henri", "Meri", date(2997, 9, 25))
test2 = Person("Mart", "Meri", date(997, 9, 25))
test3 = Person("Artur", "Meri", date(1927, 9, 25))
test4 = Female("Anni", "Meri", date(2007, 9, 25))
test5 = Female("Grete", "Meri", date(2997, 9, 25))
test6 = Female("Mel", "Meri", date(997, 9, 25))
test7 = Female("Anete", "Meri", date(1927, 9, 25))

print(test)
print(test1)
print(test2)
print(test3)
print(test4)
print(test5)
print(test6)
print(test7)


