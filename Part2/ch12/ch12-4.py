class Hexagon:
    def __init__(self,h1=6,h2=6,h3=6,h4=6,h5=6,h6=6):
        self.h1 = h1
        self.h2 = h2
        self.h3 = h3
        self.h4 = h4
        self.h5 = h5
        self.h6 = h6

    def calculate_perimeter(self):
        return self.h1 + self.h2 + self.h3 + self.h4 + self.h5 + self.h6

hex1=Hexagon()
print(hex1.calculate_perimeter())
