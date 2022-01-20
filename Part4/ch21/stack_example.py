class Stack:
    def __init__(self) -> None:
        self.items = []              # 1. 空のstack(リスト)を作成する

    def is_empty(self):
        return not self.items        # 2. stackが空なら"True"を返す

    def push(self,item):
        self.items.append(item)      # 3. stackに"item"を"append"する

    def pop(self):
        return self.items.pop()         # 4. stackから"item"を"pop"する

    def peek(self):
        return self.items[-1]        # 5. stackの一番最後の"item"を"返す

    def size(self):
        return len(self.items)        # 6. stackのsize("len")を返す



