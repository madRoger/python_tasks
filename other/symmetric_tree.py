'''
A k-ary tree is a tree with k-children, and a tree is symmetrical
if the data of the left side of the tree is the same as the right
side of the tree.

Here's an example of a symmetrical k-ary tree.

        4
     /     \
    3        3
  / | \    / | \
9   4  1  1  4  9
'''
from collections import deque

class Node():
    
    def __init__(self, value, children=[]):
        self.value = value
        self.children = children

    def __str__(self):
        return str(self.value)


def is_symmetric(root):
    deq = deque(root.children)
    while deq:
        if len(deq) % 2 == 1:
            return False

        deqsize, vals = len(deq), []
        for _ in range(deqsize):
            node = deq.popleft()
            deq.extend(node.children)
            vals.append(node.value)

        if vals != vals[::-1]:
            return False

    return True

if __name__ == '__main__':
    tree = Node(4)
    tree.children = [Node(3), Node(3)]
    tree.children[0].children = [Node(9), Node(4), Node(1)]
    tree.children[1].children = [Node(1), Node(4), Node(9)]
    tree.children[0].children[0].children = [Node(5), Node(6), Node(7)]
    tree.children[1].children[0].children = [Node(7), Node(6), Node(5)]
    print(is_symmetric(tree))
