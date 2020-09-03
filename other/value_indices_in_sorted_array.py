'''
Given a sorted array, A, with possibly duplicated elements, find
the indices of the first and last occurrences of a target element, x.
Return -1 if the target is not found.

Example:

Input: A = [1,3,3,5,7,8,9,9,9,15], target = 9
Output: [6,8]

Input: A = [100, 150, 150, 153], target = 150
Output: [1,2]

Input: A = [1,2,3,4,5,6,10], target = 9
Output: [-1, -1]
'''
def getRange(arr, target):
    if target not in arr:
        return [-1, -1]
    
    result = []
    for index, value in enumerate(arr):
        if value == target and not result:
            result.append(index)
            
        if value > target:
            result.append(index-1)
            return result
        
    result.append(len(arr)-1)    
    return result

if __name__ == '__main__':
    print(getRange([1, 3, 3, 5, 7, 8, 9, 9, 9, 15], 9))
    print(getRange([100, 150, 150, 153], 150))
    print(getRange([1, 2, 3, 4, 5, 6, 10], 9))
    print(getRange([1, 2, 5, 5, 5, 5, 5, 6, 7], 5))
        
