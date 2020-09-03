'''
Given a binary tree, return the list of node values in zigzag order traversal.
Here's an example

# Input:
#         1
#       /   \
#      2     3
#     / \   / \
#    4   5 6   7
#
# Output: [1, 3, 2, 4, 5, 6, 7]
'''
class Node:
    
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def zigzag_order(tree):
    nodes, zigzag, result = [tree], False, []
    while nodes:
        result.extend(nodes[::-1] if zigzag else nodes)
        zigzag = not zigzag
        levelLen = len(nodes)
        for i in range(levelLen):
            if nodes[i].left is not None:
                nodes.append(nodes[i].left)
                
            if nodes[i].right is not None:
                nodes.append(nodes[i].right)
                
        del nodes[:levelLen]
        
    return [node.value for node in result]
        
if __name__ == '__main__':
    n4 = Node(4)
    n5 = Node(5)
    n6 = Node(6)
    n7 = Node(7)
    n2 = Node(2, n4, n5)
    n3 = Node(3, n6, n7)
    n1 = Node(1, n2, n3)
    print(zigzag_order(n1))
