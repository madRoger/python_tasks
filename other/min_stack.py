class minStack(object):
    
    def __init__(self):
        self.stack = []

    def push(self, x):
        self.stack.append(x)

    def pop(self):
        return self.stack.pop() if self.stack else None

    def top(self):
        return self.stack[-1] if self.stack else None

    def getMin(self):
        return min(self.stack) if self.stack else None

if __name__ == '__main__':
    x = minStack()
    x.push(-20)
    x.push(0)
    x.push(-3)
    x.push(-30)
    x.push(-13)
    print('min', x.getMin())
    print('pop', x.pop())
    print('top', x.top())
    print('min', x.getMin())
    print('pop', x.pop())
    print('pop', x.pop())
    print('pop', x.pop())
    print('pop', x.pop())
    print('min', x.getMin())
