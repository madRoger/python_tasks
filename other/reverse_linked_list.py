'''
Given a singly-linked list, reverse the list. This can be done iteratively
or recursively. Can you get both solutions?

Example:

Input: 4 -> 3 -> 2 -> 1 -> 0 -> NULL
Output: 0 -> 1 -> 2 -> 3 -> 4 -> NULL
'''
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None
  
    def printList(self):
        node, output = self, ''
        while node is not None:
            output += str(node.val)
            output += ' '
            node = node.next
            
        print(output)
     

def reverseListIterative(head):
    revList, tmpNode = None, None
    while head is not None:
        tmpNode = revList
        revList = ListNode(head.val)
        head = head.next
        revList.next = tmpNode
    
    return revList

def reverseListRecursive(head):
    if head.next is None:
        return ListNode(head.val)
    else:
        resList = reverseListRecursive(head.next)
        lastNode = resList
        while lastNode.next is not None:
            lastNode = lastNode.next
        lastNode.next = ListNode(head.val)

        return resList


if __name__ == "__main__":
    a = ListNode(4)
    a.next = ListNode(3)
    a.next.next = ListNode(2)
    a.next.next.next = ListNode(1)
    a.next.next.next.next = ListNode(0)
    b = reverseListIterative(a)
    b.printList()
    c = reverseListRecursive(b)
    c.printList()
