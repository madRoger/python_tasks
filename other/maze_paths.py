'''
A maze is a matrix where each cell can either be a 0 or 1.
A 0 represents that the cell is empty, and a 1 represents a
wall that cannot be walked through.
You can also only travel either right or down.

Given a nxm matrix, find the number of ways someone can go
from the top left corner to the bottom right corner.
You can assume the two corners will always be 0.

Example:

Input: [[0, 1, 0], [0, 0, 1], [0, 0, 0]]
# 0 1 0
# 0 0 1
# 0 0 0
Output: 2

The two paths that can only be taken in the above example are:
down -> right -> down -> right, and down -> down -> right -> right.
'''

def paths_through_maze(maze):
    rowSize, colSize = len(maze[0]), len(maze)
    arr = [[0]*rowSize for _ in range(colSize)]
    for i in range(rowSize):
        if maze[0][i]:
            break
        
        arr[0][i] = 1
        
    for j in range(colSize):
        if maze[j][0]:
            break
        
        arr[j][0] = 1
        
    for m in range(1, colSize):
        for n in range(1, rowSize):
            if not maze[m][n]:
                arr[m][n] = arr[m-1][n] + arr[m][n-1]
                
    return arr[-1][-1]
            
if __name__ == '__main__':
    print(paths_through_maze([[0, 0, 1],
                              [0, 0, 1],
                              [0, 1, 1],
                              [0, 0, 0],]))
