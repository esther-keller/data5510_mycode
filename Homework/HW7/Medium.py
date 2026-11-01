''' --------Instructions--------
Implement a Python function to search for a value in a binary search tree. 
The method should take the root of the tree and 
the value to be searched as parameters. 
It should return True if the value is found in the tree, and False otherwise.'''

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

def search(root,value):
    if root is None: 
        return False

    if value == root.value:
        return True

    if value < root.value:
        return search(root.left, value)

    if value > root.value: # i know this isn't good practice (I should use else:), but I'm doing this to visualize the structure
        return search(root.right,value)


# Build a test tree
root = None
root = insert(root, 10)
root = insert(root, 5)
root = insert(root, 15)
root = insert(root, 12)

# Test search
print(search(root, 12)) # Should print True
print(search(root, 5)) # Should print True
print(search(root, 7)) # Should print False
print(search(root, 20)) # Should print False