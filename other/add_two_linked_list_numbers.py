'''
You are given two linked-lists representing two non-negative integers.
The digits are stored in reverse order and each of their nodes contain
a single digit. Add the two numbers and return it as a linked list.

Example:

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
Explanation: 342 + 465 = 807.
'''

class ListNode(object):
  
  def __init__(self, x):
    self.val = x
    self.next = None


def addTwoNumbers(list1, list2):
    addList  = ListNode(0)
    root = addList

    if list1 is None:
        return list2

    if list2 is None:
        return list1

    oneRet = 0
    while True:
        nodeSum = oneRet
        if list1 is not None:
            nodeSum += list1.val
            list1 = list1.next
        
        if list2 is not None:
            nodeSum += list2.val
            list2 = list2.next

        addList.next = ListNode(nodeSum%10)
        addList = addList.next
        oneRet = nodeSum // 10
        if list1 is None and list2 is None:
            if oneRet == 1:
                addList.next = ListNode(1)
          
            break
    return root.next

if __name__ == "__main__":
    a = ListNode(2)
    a.next = ListNode(4)
    a.next.next = ListNode(3)

    b = ListNode(5)
    b.next = ListNode(6)
    b.next.next = ListNode(4)

    c = addTwoNumbers(a, b)

    result = []
    while c is not None:
        result.append(str(c.val))
        c = c.next
        
    print(''.join(result[::-1]))
