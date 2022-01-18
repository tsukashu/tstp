"""ch13-1,2,3まとめ
1. クラスを作成し、メソッドを追加する
2. 追加のメソッドを作成して、実行してみる
3. 子クラスの親クラスを作成し、継承させる。
4. 動作確認。
"""


class Shape:
    def __init__(self, h, w):
        self.heigth = h
        self.width = w

    def what_am_i(self):
        print("I am a shape!!")


class Rectangle(Shape):
    def calculate_perimeter(self):
        return self.width * 2 + self.heigth * 2


class Square(Shape):
    def calculate_perimeter(self):
        return self.width * 4

    def change_size(self, num):
        self.width = self.width + num
        return self.width


"""ch13-1
親クラス`Shape`のインスタンスを作成し、
メソッド`what_am_i`を実行
"""
s1 = Shape(10, 20)
s1.what_am_i()


"""ch13-2
子クラス`Rectangle`のインスタンスを作成し、
メソッド`what_am_i`と子クラスの`calculate_perimeter`メソッドを実行
"""
r1 = Rectangle(20, 30)
r1.what_am_i()
print(r1.calculate_perimeter())

"""ch13-3
子クラス`Square`のインスタンスを作成し、
子クラスの`change_size`, `calculate_perimeter`メソッドを実行

"""
s1 = Square(1, 1)
s1.change_size(10000)
print(s1.calculate_perimeter())
