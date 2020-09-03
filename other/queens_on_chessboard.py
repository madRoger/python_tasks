'''
N-Queens is the problem where you find a way to put n
queens on a nxn chess board without them being able to
attack each other. Given an integer n, return 1 possible
solution by returning all the queen's position.

Example (5 queens):
There can be many answers
[(0, 0), (1, 2), (2, 4), (3, 1), (4, 3)]

Q . . . .
. . . Q .
. Q . . .
. . . . Q
. . Q . .
'''

def n_queens(n):
    if n == 1:
        return [(0, 0)]
    
    if n in [2, 3]:
        return []
    
    odd = list(range(1, n, 2))
    even = list(range(0, n, 2))
    if n%6 == 2:
        even[0], even[1] = even[1], even[0]
        even.append(even.pop(2))
    elif n%6 == 3:
        odd.append(odd.pop(0))
        even.append(even.pop(0))
        even.append(even.pop(0))
        
    return list(enumerate(odd + even))
    
    
if __name__ == '__main__':
    print(n_queens(5))

