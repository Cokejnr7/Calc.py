
from stack import Stack

class Calculator:
    def __init__(self, expression):
        self.expression = expression
        self.stack = Stack()
        self.postfix_string = ''
        self.postfix_arr = []
        self.operators = {
            '(': 4,
            ')': -4,
            '^': 3,
            '*': 2,
            '/': 2,
            '%': 2,
            '+': 1,
            '-': 1,
        }

    def isoperand(self, data):
        return data.isdigit()

    def isoperator(self, data):
        return True if self.operators.get(data) else False

    def checker(self, word):
        if self.stack.peek() is None:
            self.stack.push(word)
        else:
            if self.stack.peek() == '(':
                self.stack.push(word)
            elif self.operators.get(word) == self.operators.get(self.stack.peek()):
                if self.operators.get(word) == 3:
                    self.stack.push(word)
                else:
                    a = self.stack.pop()
                    if a != '(' or a != ')':
                        self.postfix_string += a
                        self.postfix_arr.append(a)
                    self.checker(word)
            elif self.operators.get(word) > self.operators.get(self.stack.peek()):
                self.stack.push(word)
            elif self.operators.get(word) < self.operators.get(self.stack.peek()):
                a = self.stack.pop()
                if a != '(' or a != ')':
                    self.postfix_string += a
                    self.postfix_arr.append(a)
                self.checker(word)

    def convert(self, expression):

        for i in expression:
            if i.isalpha():
                raise ValueError('no alphabets allowed')

            elif self.isoperand(i):
                self.postfix_string += i
                self.postfix_arr.append(i)

            elif i == '(':
                self.stack.push(i)

            elif i == ')':

                while not(self.stack.is_empty()) and self.stack.peek() != '(':
                    a = self.stack.pop()
                    if a != '(' or a != ')':
                        self.postfix_string += a
                        self.postfix_arr.append(a)

                self.stack.pop()

            elif self.isoperator(i):
                self.checker(i)

        while len(self.stack) != 0:
            a = self.stack.pop()
            if a != '(' or a != ')':
                self.postfix_string += a
                self.postfix_arr.append(a)
        # print(self.postfix_string)
        # print(self.stack)

    def calc_with_operator(self, input1, input2, operator):
        if operator == '^':
            return input1 ** input2
        elif operator == '*':
            return input1 * input2
        elif operator == '/':
            return input1 / input2
        elif operator == '%':
            return input1 % input2
        elif operator == '+':
            return input1 + input2
        elif operator == '-':
            return input1 - input2

    def calculate(self):
        self.convert(self.expression)

        for i in self.postfix_arr:
            if self.isoperand(i):
                self.stack.push(i)
            elif self.isoperator(i):
                A = int(self.stack.pop())
                B = int(self.stack.pop())
                result = self.calc_with_operator(B, A, i)
                self.stack.push(result)

        return self.stack.pop()

