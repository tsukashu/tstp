import csv

"""リストinリストからcsvを作成するその１（ASCIIのみ）

リストは予め与えられたもので、一つのリストに、いくつかのリストが入っている。
リストごとに行に分割してcsvに出力する

TODO
- [x] 空行あくのが気になったんだけど、治った。
- Scriptと同じフォルダにcsvを出力するには、osモジュールのインポートや、ch9-2のような方法で。
"""

movies = [
    ['Top Gun', 'Risky Business', 'Minority Report', ],
    ['Titanic', 'The Revenant', 'Inception', ],
    ['Training Day', 'Man or Fire', 'Flight', ],
]


with open('movies.csv', 'w',newline='') as f:
    w = csv.writer(f)
    for i in movies:
        w.writerow(i)
