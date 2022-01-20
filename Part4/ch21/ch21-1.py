class Stack:
    def __init__(self) -> None:
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def size(self):
        return len(self.items)


c = "yesterday"
s1 = Stack()
for i in c:
    s1.push(i)

# print(s1.size())

r1 = []  # <-if if is iterable, it works.
while s1.size():
    r1 = s1.pop()
print(r1)

# for test and debug
# while s1.size():
# ?? `r1 += a ` may be increment index, menbe...
# a = s1.pop()
# r1 += a
# print(a)
# print(r1)
