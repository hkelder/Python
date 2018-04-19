# Write a program in which you have a class, and you can instantiate object of it.
# However, there is a restriction that you can create maximum of 1 object.
# When 1 single object has been created out of that class, we must not be able to create more objects.
# Code within the class is irrelevant but it should support only one object.


class Hello:
    sharedState = {}

    def __init__(self):
        self.__dict__ = self.sharedState


class Singleton(Hello):
    def __init__(self, arg):
        Hello.__init__(self)
        self.val = arg

    def __str__(self):
        return self.val


iteration1 = Singleton("Egg")  # Since singleton replaces the previous iteration value, you can only have 1 value always
print(iteration1)

iteration2 = Singleton("Bacon")
print(iteration2)
print(iteration1)

iteration3 = Singleton("123")
print(iteration3)
print(iteration2)
print(iteration1)
