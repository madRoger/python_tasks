'''
Create a function that takes a positive integer and returns the next bigger
number that can be formed by rearranging its digits. For example:

12 ==> 21
513 ==> 531
2017 ==> 2071

nextBigger(num: 12)   // returns 21
nextBigger(num: 513)  // returns 531
nextBigger(num: 2017) // returns 2071

If the digits can't be rearranged to form a bigger number, return -1 (or nil in Swift):

9 ==> -1
111 ==> -1
531 ==> -1

nextBigger(num: 9)   // returns nil
nextBigger(num: 111) // returns nil
nextBigger(num: 531) // returns nil
'''
def next_bigger(n):
    digs = [int(dig) for dig in str(n)]
    tail = []
    for i in reversed(range(1, len(digs))):
        tail.append(digs[i])
        if digs[i] > digs[i-1]:
            for j in range(len(tail)):
                if tail[j] > digs[i-1]:
                    digs[i-1], tail[j] = tail[j], digs[i-1]
                    digs = digs[:i] + tail
                    break
                
            break
        
    result = int(''.join([str(num) for num in digs]))
    return result if result != n else -1
 
if __name__ == '__main__':
    print(next_bigger(2017))
    
