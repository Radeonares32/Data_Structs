class LinkedList():
    def __init__(self,value):
        self.value = value
        self.nextNode = None
    def setNextNode(self,node):
        self.nextNode = node
    def getNextNode(self):
        return self.nextNode
    def getNodeValue(self):
        return self.value

ankara = LinkedList("06")
adana = LinkedList("01")
istanbul = LinkedList("31")

ankara.setNextNode(adana)
print(ankara.getNextNode().getNodeValue())