class Queue:
    def __init__(self):
        self.array = []
    def isEmpty(self):
        return self.array == []
    def enqueue(self,item):
        self.array.insert(0,item)
    def dequeue(self):
        self.array.pop()
    def prnt(self):
        for items in self.array:
            print(items)

deq = Queue()

print(deq.isEmpty())
deq.enqueue(10)
deq.enqueue(20)
deq.enqueue(30)
deq.dequeue()
print(deq.isEmpty())
deq.prnt()