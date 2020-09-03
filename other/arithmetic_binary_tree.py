'''
You are given a binary tree representation of an arithmetic expression.
In this tree, each leaf is an integer value,, and a non-leaf node is one
of the four operations: '+', '-', '*', or '/'.

Write a function that takes this tree and evaluates the expression.

Example:

    *
   / \
  +    +
 / \  / \
3  2  4  5


This is a representation of the expression (3 + 2) * (4 + 5), and should
return 45.
'''

class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

PLUS = lambda x, y: x + y
MINUS = lambda x, y: x - y
TIMES = lambda x, y: x * y
DIVIDE = lambda x, y: x / y

OPS = [PLUS, MINUS, TIMES, DIVIDE]

def evaluate(root):
    if root.val in OPS:
        return root.val(evaluate(root.left), evaluate(root.right))

    return root.val

if __name__ in '__main__':
    tree = Node(PLUS)
    tree.left = Node(MINUS)
    tree.left.left = Node(PLUS)
    tree.left.left.left = Node(2)
    tree.left.left.right = Node(3)
    tree.left.right = Node(TIMES)
    tree.left.right.left = Node(6)
    tree.left.right.right = Node(2)
    tree.right = Node(DIVIDE)
    tree.right.left = Node(100)
    tree.right.right = Node(5)
    print(evaluate(tree))
