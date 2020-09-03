'''
Given a number of integers, combine them so it would create the largest number.

Example:

Input:  [17, 7, 2, 45, 72]
Output:  77245217
'''
from functools import cmp_to_key

def cmpr(x, y):
    x, y = str(x), str(y)
    if x[0] == y[0]:
        while len(x) > len(y):
            y += y[0]
            
        while len(x) < len(y):
            x += x[0]
            
    return 1 if x > y else -1

def largestNum(nums):
    nums.sort(key = cmp_to_key(cmpr), reverse = True)
    return ''.join(map(str, nums))
    
if __name__ == '__main__':
    print(largestNum([17, 7, 2, 45, 72]))
