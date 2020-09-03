'''
You are given the root of a binary search tree.
Return true if it is a valid binary search tree, and false otherwise.
Recall that a binary search tree has the property that all values in
the left subtree are less than or equal to the root, and all values in
the right subtree are greater than or equal to the root.
'''
from collections import deque

class TreeNode:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.key = key

def is_bst(root):
    deq = deque([root])
    while deq:
        node = deq.popleft()
        if node.left:
            if node.left.key > node.key:
                return False
            deq.append(node.left)
            
        if node.right:
            if node.right.key < node.key:
                return False
            deq.append(node.right)
            
    return True
    
if __name__ == '__main__':
    a = TreeNode(5)
    a.left = TreeNode(3)
    a.right = TreeNode(7)
    a.left.left = TreeNode(1)
    a.left.right = TreeNode(4)
    a.right.left = TreeNode(6)
    print(is_bst(a))
