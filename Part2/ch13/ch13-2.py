class Rectangle:
    def __init__(self, w, h):
        self.width = w
        self.height = h

    def calculate_perimeter(self):
        return self.width * 2 + self.heigh * 2


class Square:
    def __init__(self, w):
        self.width = w

    def calculate_perimeter(self):
        return self.width * 4

    def change_size(self, num):
        self.width = self.width + num
        return self.width
