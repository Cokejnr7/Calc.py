


class Stack:
    def __init__(self):
        self.stack = []
        self.size_of_stack = 0

    def peek(self):
        if self.stack == []:
            return
        return self.stack[-1]

    def push(self, data):
        self.stack.append(data)
        self.size_of_stack += 1

    def pop(self):
        if self.stack == []:
            return None

        data = self.stack[-1]
        del self.stack[-1]
        self.size_of_stack -= 1
        return data

    def is_empty(self):
        return False if self.size_of_stack != 0 else True

    def traverse(self):
        for i in range(len(self.stack)-1, 0, -1):
            print(self.stack[i])

    def __len__(self):
        return self.size_of_stack

    def __repr__(self):

        val = "Stack"+str(list(reversed(self.stack)))
        return val
