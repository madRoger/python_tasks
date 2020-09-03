'''
You are given an array of integers. Return all the permutations of this array.
You can't use itertools.permutations
'''

def permute(nums):
    if not nums:
        return None
    
    res = [[num] for num in nums]
    while True:
        if len(res[0]) == len(nums):
            break
        
        levelLen = len(res)
        for i in range(levelLen):
            for num in [n for n in nums if n not in res[i]]:
                res.append(res[i] + [num])
                
        del res[:levelLen]
        
    return res
  
if __name__ == '__main__':
    print(permute([1, 2, 3]))
