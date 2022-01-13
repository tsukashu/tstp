#https://uxmilk.jp/14834

set
"""
- iterable
- unorderd collection
- **unique elements**

Example:
"""
s1 = set([1,2,3,4,5])     # set([1,2,3,4,5]) 
s2 = set([1,1,2,2,3,3])   # set([1,2,3])
sd = set({
            'dog':'inu',
            'cat':'neko',
            'bird':'tori'
        })   # set(['dog', 'cat', 'bird'])

print(s1)
print(s2)
print(sd)

"""
追加するにはadd
削除するにはremove
など使う

その他集合のについてのあれこれもあるらしいが、そのへん苦手なんでこの辺で…
"""