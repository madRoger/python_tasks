'''
Given a binary tree and an integer k, filter the binary tree such that
its leaves don't contain the value k. Here are the rules:

- If a leaf node has a value of k, remove it.
- If a parent node has a value of k, and all of its children are removed,
remove it.
'''
class Node:
    
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    def __repr__(self):
        return f"value: {self.value}, left: ({self.left.__repr__()}), right: ({self.right.__repr__()})"


def filter(tree, k):
    if tree.left is not None and filter(tree.left, k):
            tree.left = None
            
    if tree.right is not None and filter(tree.right, k):
            tree.right = None
            
    return (tree.left is None and
            tree.right is None and
            tree.value == k)
    
if __name__ == '__main__':
    n5 = Node(2)
    n4 = Node(1)
    n3 = Node(1, n4)
    n2 = Node(1, n5)
    n1 = Node(1, n2, n3)
    filter(n1, 1)
    print(n1)
