'''
You are given an array of k sorted singly linked lists.
Merge the linked lists into a single sorted linked list and return it.
'''

class Node(object):
    
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        c = self
        answer = ""
        while c:
            answer += str(c.val) + " " if c.val else ""
            c = c.next
        return answer

def merge(lists):
    mergedList, root = None, None
    while True:
        minInd = -1
        for i in range(0, len(lists)):
            if lists[i] is not None:
                if minInd == -1 or lists[minInd].val > lists[i].val:
                    minInd = i
                    
        if minInd == -1:
            return root
        
        if mergedList is None:
            mergedList = Node(lists[minInd].val)
            root = mergedList
        else:
            mergedList.next = Node(lists[minInd].val)
            mergedList = mergedList.next
            
        lists[minInd] = lists[minInd].next
    

if __name__ == '__main__':
    a = Node(1, Node(9, Node(15)))
    b = Node(2, Node(4, Node(25)))
    c = Node(7, Node(8, Node(20)))
    print(merge([a, b, c]))
