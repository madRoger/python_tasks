'''
You are given the root of a binary tree. Find the path between 2 nodes
that maximizes the sum of all the nodes in the path, and return the sum.
The path does not necessarily need to go through the root.

Example:
        10
       /  \
      2     10
     / \     \
    20  1    -25
             /  \
            3    4

max path from left leaf(20) to right root node (10) sum = 42
'''

class Node:
    
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


maxSum = float("-inf")

def maxPathSum(root):
    global maxSum
    localSum = root.val
    leftVal, rightVal = 0, 0
    if root.left is not None:
        leftVal = maxPathSum(root.left)
        if leftVal < 0:
            leftVal = 0
    if root.right is not None:
        rightVal = maxPathSum(root.right)
        if rightVal < 0:
            rightVal = 0
    if (localSum + leftVal + rightVal) > maxSum:
        maxSum = localSum + leftVal + rightVal
    localSum += max(leftVal, rightVal)
    return localSum


if __name__ == '__main__':
    root = Node(10)
    root.left = Node(2)
    root.right = Node(10)
    root.left.left = Node(20)
    root.left.right = Node(1)
    root.right.right = Node(-25)
    root.right.right.left = Node(3)
    root.right.right.right = Node(4)
    maxPathSum(root)
    print(maxSum)
