class Square:
    square_list = []

    def __init__(self, w, l) -> None:
        self.width = w
        self.length = l
        self.square_list.append((self.width, self.length))


s1 = Square(10, 10)
s2 = Square(20, 10)
s3 = Square(30, 30)
print(Square.square_list)
