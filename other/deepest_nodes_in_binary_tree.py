'''
You are given the root of a binary tree.
Return the deepest node(s) (the furthest node(s) from the root).

Example:

    a
   / \
  b   c
 /
d

The deepest node in this tree is d at depth 3.
'''

from collections import deque

class Node(object):
    
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def deepest(node):
    deq = deque([node])
    level, nodes = 0, []
    while deq:
        level += 1
        parents = len(deq)
        nodes.clear()
        for _ in range(parents):
            node = deq.popleft()
            nodes.append(node.val)
            if node.left is not None:
                deq.append(node.left)

            if node.right is not None:
                deq.append(node.right)
                
    return (','.join(nodes), level)
  
if __name__ == '__main__':
    root = Node('a')
    root.left = Node('b')
    root.left.left = Node('d')
    root.right = Node('c')
    print(deepest(root))
