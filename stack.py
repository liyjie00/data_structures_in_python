class Stack(object):
    def __init__(self):
        self.stack = []

    def printStack(self):
        print(self.stack)

    def push(self, value):
        self.stack.append(value)

    def pop(self):
        if len(self.stack) == 0:
            print('The stack is empty')
        else:
            self.stack.pop()

    def peek(self):
        return self.stack[-1]

    def size(self):
        return len(self.stack)


if __name__ == '__main__':
    myStack = Stack()
    myStack.push(11)
    myStack.push(22)
    myStack.push(33)
    myStack.push(44)
    myStack.push(55)
    myStack.printStack()
    print('-' * 30)
    myStack.pop()
    myStack.printStack()
