class Node:
    def __init__(self,key):
        self.val = key
        self.left = None
        self.right = None

def insert(root,node)->Node:
    if root is None:
        root = node
        if root.right is None:
            root.right = node
        else:
            insert(root.right,node)
    else:
        if root.left is None:
            root.left = node
        else:
            insert(root.left,node)
def inorder(root):
    if root:
        inorder(root.left)
        print(root.val)
        inorder(root.right)
    else:
        return None

r = Node(41)
insert(root=r,node=120)
inorder(r)


