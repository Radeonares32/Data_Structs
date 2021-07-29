class Stack:
    def __init__(self):
        self.items = []
    def isEmpty(self):
        return self.items == []
    def push(self,item):
        self.items.append(item)
    def pop(self):
        self.items.pop()
    def bottom(self):
        return self.items[len(self.items)-1]
    def top(self):
        return self.items[0]
    def size(self):
        return len(self.items)
    def prnt(self):
        for item in self.items:
            print(item)
stack = Stack()

print(stack.isEmpty())
stack.push(10)
stack.push(20)
stack.push(30)
stack.pop()
print(stack.isEmpty())
print("---------------")
print(stack.top())
print("---------------")
print(stack.bottom())
print("---------------")
print(stack.size())
stack.prnt()