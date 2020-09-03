'''
Given a sequence of numbers, find the longest
sequence that contains only 2 unique numbers.

Example:

Input: [1, 3, 5, 3, 1, 3, 1, 5]
Output: 4
'''
from collections import OrderedDict

def findSequence(seq):
    nums = OrderedDict.fromkeys(seq)
    if len(nums) < 2:
        return 0

    twoFirst, biList = list(nums.keys())[:2], []
    for num in seq:
        if num not in twoFirst:
            break
        
        biList.append(num)

    maxLen = len(biList)
    for num in seq[len(biList):]:
        if num in biList:
            biList.append(num)
        else:
            if len(biList) > maxLen:
                maxLen = len(biList)

            while biList.count(biList[-1]) != len(biList):
                del biList[0]
                
            biList.append(num)

    return maxLen

if __name__ == '__main__':
    print(findSequence([1, 3, 5, 3, 1, 3, 1, 5]))
    print(findSequence([1, 3, 5, 2, 1, 2, 7, 1, 1, 3, 7, 5]))
