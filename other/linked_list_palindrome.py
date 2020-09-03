'''
You are given a doubly linked list. Determine if it is a palindrome.
'''
class Node(object):
    
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None


def is_palindrome(node):
    if node.next is None:
        return False
    
    leftNode, rightNode = node, node
    while rightNode.next is not None:
        rightNode = rightNode.next
        
    while True:
        if leftNode.val != rightNode.val:
            return False
        
        if (leftNode.next == rightNode.prev or
            leftNode.next == rightNode):
            break
        
        leftNode, rightNode = leftNode.next, rightNode.prev
        
    return True

def is_palindrome2(node):
    if node.next is None:
        return False
    
    lst = []
    while node is not None:
        lst.append(node.val)
        node = node.next
        
    return lst == lst[::-1]


if __name__ == '__main__':
    node = Node('a')
    node.next = Node('b')
    node.next.prev = node
    node.next.next = Node('b')
    node.next.next.prev = node.next
    node.next.next.next = Node('a')
    node.next.next.next.prev = node.next.next
    print(is_palindrome(node))
    print(is_palindrome2(node))
