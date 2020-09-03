'''
Your task, is to create a NxN spiral with a given size.

For example, spiral with size 5 should look like this:

00000
....0
000.0
0...0
00000

and with the size 10:

0000000000
.........0
00000000.0
0......0.0
0.0000.0.0
0.0..0.0.0
0.0....0.0
0.000000.0
0........0
0000000000

Return value should contain array of arrays, of 0 and 1,
for example for given size 5 result should be:

[[1,1,1,1,1],[0,0,0,0,1],[1,1,1,0,1],[1,0,0,0,1],[1,1,1,1,1]]

Because of the edge-cases for tiny spirals, the size will be at least 5.

General rule-of-a-thumb is, that the snake made with '1' cannot touch to itself.


'''
def spiralize(size):
    mat = [[1]*size for _ in range(size)]
    mat[1][:-1], row, column = [0]*(size-1), 1, size-2
    spirs = sorted([x for x in range(size-3, 0, -2)]*2, reverse=True)
    if len(spirs)%4:
        spirs.extend([0]*(4-len(spirs)%4))
        
    for sp in spirs:
        mat = [list(tpl) for tpl in reversed(list(zip(*mat)))]
        if sp:
            row, column = (size-1) - column, row + 1
            mat[row][column:column+sp] = [0]*sp
            column += sp - 1
            
    return mat

 
if __name__ == '__main__':
    print(spiralize(5))

    
