import csv

"""リストinリストからcsvを作成するその２（非ASCII）

要件はch9-3と一緒。
唯一、日本語のリスト（非ASCII）であることなので、コピペでエンコーディングだけ足しました。

"""

movies_u = [
    ['トップガン', 'リスキービジネス', 'マイノリティーリポート', ],
    ['タイタニック', 'レヴェナント', 'インセプション', ],
    ['以下略',],
]


with open('movies_u.csv', 'w', newline='', encoding='utf-8') as f:
    w = csv.writer(f)
    for i in movies_u:
        w.writerow(i)
