''' --------Instructions--------
Explain the process of deleting a node from a binary search tree in Python. 
Discuss how you would handle different cases, such as deleting a node with one, 
or two children. 
Additionally, explain any potential challenges or edge cases that may arise 
during the deletion process and how you would address them. '''

'''
No Children:
If a node has no children, we can simply remove it by returning None. 
It won't have any effect on the surrounding tree structure because it is a leaf node.


1 Child: 
If a node has 1 child, the child moves up and replaces the deleted node. 
It will have a small effect on the surrounding tree structure beccause
the deleted node is replaced by its only child, making it so that the rest of the 
subtree remains unchanged.

2 Children:
BST deletion algorithms chose betwen either taking the largest value fromt the 
left subtree  or the smallest value from the right subtree (the in-order successor)
 to replace the deleted node. These values are chosen becuause they presever the 
 BST ordering protocol after deletion.
Once a node has been copied into the deleted nodes position, we can delete it 
from it's origional spot on the BST. 

Challenges / Edge cases: 
1. a tree is empty, and we try to delete a node 
    - there is no node to delete (root is None). The function should return None 
    and leave the tree unchanged.
2. we're deleting a root node
    - We need to replace the root node. The algorithm has to return a new root 
    of the tree after the deletion is complete.  The new Node will come from a 
    node within the tree structure. The algorith will have to reutrn the new root 
    of the tree after the deletion is complete. After that, depending on what 
    the situation was with that node, you follow the steps if it has 0,1, or 2 
    children.
3. the value we're trying to dele doesn't exist in the tree
    - no changes will be made to the tree. The algorithm will simply return 
    the origional tree. 

''' 