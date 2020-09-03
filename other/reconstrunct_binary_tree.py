'''
You are given the preorder and inorder traversals of a binary tree in the
form of arrays. Write a function that reconstructs the tree represented by
these traversals.

Example:
Preorder: [a, b, d, e, c, f, g]
Inorder: [d, b, e, a, f, c, g]

The tree that should be constructed from these traversals is:

    a
   / \
  b   c
 / \ / \
d  e f  g
'''
from collections import deque

class Node(object):
    
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

    def __str__(self):
        q = deque()
        q.append(self)
        result = ''
        while len(q):
            n = q.popleft()
            result += n.val
            if n.left:
                q.append(n.left)
                
            if n.right:
                q.append(n.right)
                
        return result


def reconstruct(preorder, inorder):
    root = preorder[0]
    leftCount = inorder.index(root)
    leftNodes = preorder[1:leftCount+1]
    leftNodes.reverse()
    rightNodes = preorder[leftCount+1:len(preorder)]
    rightNodes.reverse()
    node = Node(root)
    if leftNodes:
        node.left = Node(leftNodes.pop())
        
    deq = deque([node.left])
    while leftNodes:
        parent = deq.popleft()
        parent.left = Node(leftNodes.pop())
        deq.append(parent.left)
        if leftNodes:
            parent.right = Node(leftNodes.pop())
            deq.append(parent.right)
            
    if rightNodes:
        node.right = Node(rightNodes.pop())
        
    deq = deque([node.right])
    while rightNodes:
        parent = deq.popleft()
        parent.left = Node(rightNodes.pop())
        deq.append(parent.left)
        if rightNodes:
            parent.right = Node(rightNodes.pop())
            deq.append(parent.right)
            
    return node

if __name__ == '__main__':
    tree = reconstruct(['a', 'b', 'd', 'e', 'c', 'f', 'g'],
                       ['d', 'b', 'e', 'a', 'f', 'c', 'g'])
    print(tree)
