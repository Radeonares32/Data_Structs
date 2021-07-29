class Deque:
    def __init__(self):
        self.data = []
    def isEmpty(self):
        return self.data == []
    def addFront(self,item):
        self.data.append(item)
    def addBack(self,item):
        self.data.insert(0,item)
    def removeFront(self):
        self.data.pop()
    def removeBack(self):
        self.data.pop(0)
    def size(self):
        return len(self.data)
    def prnt(self):
        for i in self.data:
            print(i)
deque = Deque()

print(deque.isEmpty())
deque.addFront(10)
deque.addFront(20)
deque.removeFront()
deque.addBack(30)
deque.prnt()
print(deque.isEmpty())
print(deque.size())