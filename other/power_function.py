'''
The power function calculates x raised to the nth power.
If implemented in O(n) it would simply be a for loop over n
and multiply x n times. Instead implement this power function in O(log n) time. You can assume that n will be a non-negative integer.
'''

def pow(x, n):
    rest = 1
    while n > 1:
        n, r = divmod(n , 2)
        if r:
            rest *= x
            
        x *= x
        
    return x * rest

if __name__ == '__main__':
    print(pow(5, 3))
