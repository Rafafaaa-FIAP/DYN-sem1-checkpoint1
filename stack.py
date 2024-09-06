
class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if (self.is_empty()):
            raise IndexError('A pilha está vazia!')
        return self.items.pop()

    def size(self):
        return len(self.items)

    def peek(self):
        if (self.is_empty()):
            raise IndexError('A pilha está vazia!')
        return self.items[-1]

    def __str__(self):
        result = ''
        for i in reversed(self.items):
            result += f'\n|{i}|'
        return result