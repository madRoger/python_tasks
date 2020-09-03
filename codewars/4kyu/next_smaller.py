'''
Write a function that takes a positive integer and returns the next smaller
positive integer containing the same digits.

For example:

next_smaller(21) == 12
next_smaller(531) == 513
next_smaller(2071) == 2017

Return -1 (for Haskell: return Nothing, for Rust: return None), when there
is no smaller number that contains the same digits. Also return -1 when the
next smaller number with the same digits would require the leading digit to
be zero.

next_smaller(9) == -1
next_smaller(135) == -1
next_smaller(1027) == -1  # 0721 is out since we don't write numbers with
leading zeros

    some tests will include very large numbers.
    test data only employs positive integers.
'''
def next_smaller(n):
    digs = [int(dig) for dig in str(n)]
    tail = []
    for i in reversed(range(1, len(digs))):
        tail.append(digs[i])
        if digs[i] < digs[i-1]:
            for j in range(len(tail)):
                if tail[j] < digs[i-1]:
                    digs[i-1], tail[j] = tail[j], digs[i-1]
                    digs = digs[:i] + tail
                    break
                
            break
        
    if not digs[0]:
        return -1
    
    result = int(''.join([str(num) for num in digs]))
    return result if result != n else -1 
if __name__ == '__main__':
    print(next_smaller(2071))
    
