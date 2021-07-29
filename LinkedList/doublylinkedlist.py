class DoublyLinkedLisyt:
    def __init__(self,value):
        self.value = value
        self.nextnode = None
        self.prevnode = None
    def setNextNode(self,node):
        self.nextnode = node
    def setPrevNode(self,node):
        self.prevnode = node
    def getNextNode(self):
        return self.nextnode
    def getPrevNode(self):
        return self.prevnode
    def getValue(self):
        return self.value

dblnklist = DoublyLinkedLisyt("Bugra")
dblnklist1 = DoublyLinkedLisyt("Ahmet")
dblnklis2 = DoublyLinkedLisyt("Osman")

dblnklist.setNextNode(dblnklis2)

dblnklist1.setPrevNode(dblnklis2)

print(dblnklist1.getPrevNode().getValue())
print(dblnklist.getNextNode().getValue())