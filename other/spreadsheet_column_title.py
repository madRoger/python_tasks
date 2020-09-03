'''
MS Excel column titles have the following pattern: A, B, C, ..., Z, AA,
AB, ..., AZ, BA, BB, ..., ZZ, AAA, AAB, ... etc. In other words,
column 1 is named "A", column 2 is "B", column 26 is "Z", column 27 is "AA"
and so forth. Given a positive integer, find its corresponding column name.
Examples:

Input: 26
Output: Z

Input: 51
Output: AY

Input: 52
Output: AZ

Input: 676
Output: YZ

Input: 702
Output: ZZ

Input: 704
Output: AAB
'''
def convertToTitle(n):
    if n < 1:
        return None
        
    letterList = []
    while n > 26:
        if n%26 == 0:
            letterList = ['Z'] + letterList
            n -= 1
        else:
            letterList = [chr(n % 26 + 64)] + letterList
            
        n //= 26
    letterList = [chr(n + 64)] + letterList
    return ''.join(letterList)

if __name__ == '__main__':
    print(convertToTitle(1))
    print(convertToTitle(456976))
    print(convertToTitle(28))

