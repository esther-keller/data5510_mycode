''' --------Instructions--------
Write a Python function to insert a value into a binary search tree. 
The function should take the root of the tree and 
the value to be inserted as parameters.'''

class Node: 
    def __init__(self,value):
        self.value = value
        self.left = None
        self.right = None

def insert(root,value):
    if root is None: 
        return Node(value)

    if value < root.value:
        root.left = insert(root.left, value)
    else:
        root.right = insert(root.right, value)

    return root

def inorder(root):
    if root:
        inorder(root.left)
        print(root.value)
        inorder(root.right)


root = None

root = insert(root, 10)
root = insert(root, 5)
root = insert(root, 15)
root = insert(root, 12)

inorder(root)