import math


class Circle:
    def __init__(self, r):
        self.r = r

    def area(self):
        return math.pi * self.r * self.r


c1 = Circle(10)
print(c1.area())

c2 = Circle(20)
print(c2.area())
