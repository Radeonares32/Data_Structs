class Node:
    def __init__(self,value):
        self.value = value
        self.right = None
        self.left = None

node = Node("A")
node.left = Node("B")
node.right = Node("C")
node.left.right = Node("D")