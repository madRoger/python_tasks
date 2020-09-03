'''
Given a list of words, group the words that are anagrams of each other.
(An anagram are words made up of the same letters).

Example:

Input: ['abc', 'bcd', 'cba', 'cbd', 'efg']
Output: [['abc', 'cba'], ['bcd', 'cbd'], ['efg']]
'''

def groupAnagramWords(strs):
    strSet, resultList = [set(n) for n in strs], []
    for i in range(0, len(strSet)-1):
        if strSet[i] is None:
            continue
        
        subList = [strs[i]]
        for j in range(i+1, len(strSet)):
            if strSet[j] is None:
                continue
            
            if strSet[i] == strSet[j]:
                subList.append(strs[j])
                strSet[j] = None
                
        resultList.append(subList)
        
    if strSet[-1] is not None:
        resultList.append([strs[-1]])
        
    return resultList

if __name__ == '__main__':
    print(groupAnagramWords(['abcccd', 'bcd', 'ggefg', 'cba', 'cbd', 'efg']))

