'''
A binary gap within a positive number num is any sequence of consecutive zeros
that is surrounded by ones at both ends in the binary representation of num.
For example:
9 has binary representation 1001 and contains a binary gap of length 2.
529 has binary representation 1000010001 and contains two binary gaps: one of
length 4 and one of length 3.
20 has binary representation 10100 and contains one binary gap of length 1.
15 has binary representation 1111 and has 0 binary gaps.
Write function gap(num) that,  given a positive num,  returns the length of its
longest binary gap.
The function should return 0 if num doesn't contain a binary gap.
'''
def gap(num):
    if num < 0:
        return -1
    
    globalGap, localGap, noOnes = 0, 0, True
    while num:
        if noOnes:
            if num & 1:
                noOnes = False
                
            num >>= 1
            continue
        
        if num & 1:
            if localGap > globalGap:
                globalGap = localGap
                
            localGap = 0
        else:
            localGap += 1
            
        num >>= 1
        
    return globalGap

 
if __name__ == '__main__':
    print(gap(9))
    print(gap(529))
