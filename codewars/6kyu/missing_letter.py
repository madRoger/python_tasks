'''
Write a method that takes an array of consecutive (increasing) letters as input
and that returns the missing letter in the array.

You will always get an valid array. And it will be always exactly one letter be
missing. The length of the array will always be at least 2.
The array will always contain letters in only one case.

Example:

['a','b','c','d','f'] -> 'e' ['O','Q','R','S'] -> 'P'

["a","b","c","d","f"] -> "e"
["O","Q","R","S"] -> "P"

(Use the English alphabet with 26 letters!)
'''
def find_missing_letter(chars):
    nums = [ord(word) for word in chars] 
    for i in range(len(chars)-1):
        if nums[i] != nums[i+1] - 1:
            return chr(nums[i] + 1)
        
    return ''

 
if __name__ == '__main__':
    print(find_missing_letter(['a','b','c','d','f']))
