class Square:
    def __init__(self, l):
        self.length = l

    def __repr__(self):
        return "{} by {} by {} by {}".format(
            self.length, self.length, self.length, self.length
        )
        # return print("{}by{}by{}by{}"~)) <= It cause Type error; print() return 'non-type'.
        # https://stackoverflow.com/questions/49616600/typeerror-str-returned-non-string-type-nonetype


s1 = Square(10)
print(s1)
