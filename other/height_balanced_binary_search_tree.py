'''
Given a sorted list, create a height balanced binary search tree,
meaning the height differences of each node can only differ by at most 1.

Example:
create_height_balanced_bst([1, 2, 3, 4, 5, 6, 7, 8])
#  (pre-order traversal)
#       5
#      / \
#     3    7
#    / \  / \
#   2   4 6  8
#  /
# 1

# 53214768
'''
class Node:
    
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    def __str__(self):
        answer = str(self.value)
        if self.left:
            answer += str(self.left)
            
        if self.right:
            answer += str(self.right)
            
        return answer


def create_height_balanced_bst(nums):
    numsLen = len(nums)
    if numsLen == 0:
        return None
    
    if numsLen == 1:
        return Node(nums[0])
    
    midIndex = numsLen // 2
    node = Node(nums[midIndex])
    node.left = create_height_balanced_bst(nums[:midIndex])
    if (numsLen - 1) > midIndex:
        node.right = create_height_balanced_bst(nums[midIndex+1:numsLen])
        
    return node

if __name__ == '__main__':
    tree = create_height_balanced_bst([1, 2, 3, 4, 5, 6, 7, 8])
    print(tree)
