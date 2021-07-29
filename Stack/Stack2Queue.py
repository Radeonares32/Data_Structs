class Stack2Queue:
    def __init__(self):
        self.stack1 = []
        self.stack2 = []
    def enqueue(self,item):
        self.stack1.append(item)
    def dequeue(self):
        if not self.stack2:
            while len(self.stack1) > 0:
                self.stack2.append(self.stack1.pop())
        return self.stack2.pop()

deque = Stack2Queue()

deque.enqueue("1")
deque.enqueue("2")
deque.enqueue("3")
print(deque.dequeue())