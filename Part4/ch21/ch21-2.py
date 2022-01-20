class Stack:
    def __init__(self) -> None:
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def size(self):
        return len(self.items)


stack = Stack()
for i in [1, 2, 3, 4, 5]:
    stack.push(i)

rnumbers = []
while stack.size():
    rnumbers += str(stack.pop())
    # int cause TypeError
print(rnumbers)
