'''
Given a binary tree, return all values given a certain height.
'''
from collections import deque

class Node():
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

def valuesAtHeight(root, height):
    deq = deque([root])
    level, nodes = 0, []
    while deq:
        level += 1
        nodes.clear()
        deqsize = len(deq)
        for _ in range(deqsize):
            node = deq.popleft()
            nodes.append(node.value)
            if node.left:
                deq.append(node.left)
                
            if node.right:
                deq.append(node.right)

        if level == height:
            return nodes
                
    return None

if __name__ == '__main__':
    a = Node(1)
    a.left = Node(2)
    a.right = Node(3)
    a.left.left = Node(4)
    a.left.right = Node(5)
    a.right.right = Node(7)
    print(valuesAtHeight(a, 3))
