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
for i in "yesterday":
    stack.push(i)

# print(stack.size())

reverse_stack = []  # <-if if is iterable, it works.
while stack.size():
    reverse_stack += stack.pop()
print(reverse_stack)

# for test and debug
# while stack.size():
# ?? `reverse_stack += a ` may be increment index, menbe...
# a = stack.pop()
# reverse_stack += a
# print(a)
# print(reverse_stack)
