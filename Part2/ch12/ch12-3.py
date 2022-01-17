class Triangle:
    def __init__(self, b, h):
        self.base = b
        self.height = h

    def area(self):
        return (1 / 2) * self.base * self.height


t1 = Triangle(3, 5)
print(t1.area())

t2 = Triangle(10, 30)
print(t2.area())
