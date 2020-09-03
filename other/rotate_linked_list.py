'''
Given a linked list and a number k, rotate the linked list by k places.
'''
class Node:
    
    def __init__(self, value, nxt=None):
        self.value = value
        self.next = nxt
        
    def __str__(self):
        current = self
        ret = ''
        while current:
            ret += str(current.value)
            current = current.next
            
        return ret


def rotate_list(node, k):
    if k < 1:
        return node
    
    endNode = node
    while endNode.next is not None:
        endNode = endNode.next
        
    endNode.next = node
    while k > 1:
        node = node.next
        k -= 1
        
    result = node.next
    node.next = None
    return result

if __name__ == '__main__':
    llist = Node(1, Node(2, Node(3, Node(4))))
    print(rotate_list(llist, 2))
