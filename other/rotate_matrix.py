'''
Given a square 2D matrix (n x n), rotate the matrix by 90 degrees clockwise.

Here's an example:

before:
# 1 2 3
# 4 5 6
# 7 8 9

after:
# 7 4 1
# 8 5 2
# 9 6 3
'''

def rotate(mat):
    return [list(t) for t in zip(*mat[::-1])]

if __name__ == '__main__':
    mat = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    print(rotate(mat))
