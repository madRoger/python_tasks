'''
Your task will be to return the number of arrangements that evaluate to True.

t,f will stand for true, false and the operators will be Boolean AND (&), OR (|), and XOR (^).

For example, solve("tft","^&") = 2, as follows:

    "((t ^ f) & t)" = True
    "(t ^ (f & t))" = True

Notice that the order of the boolean values and operators does not change.
What changes is the position of braces. 
'''

def calc_tree(root, work):
    sums = 0
    for key, dct in root.items():
        work_copy = [val[:] for val in work]
        for i in range(len(work_copy)):
            if work_copy[i][1] == key:
                body = work_copy[i]
                bol = body[2](body[0], body[-1])
                if i:
                    work_copy[i-1][-1] = bol
                    
                if i < len(work_copy)-1:
                    work_copy[i+1][0] = bol
                    
                del work_copy[i]
                break
            
        if dct:
            sums += calc_tree(dct, work_copy)
        else:
            body = work_copy[0]
            sums += int(body[2](body[0], body[-1]))
            
    return sums

def combs(size):
    def perms(cons, size):
        store, head, tail = [], cons[:size], cons[size:]
        for i in range(1, len(tail)+1):
            store.append(tail[:i] + head + tail[i:])
            for j in range(1, size):
                for cons in perms(head + tail[i:], j):
                    store.append(tail[:i] + cons)
                    
        return store
    
    arr = [list(range(size))]
    for num in range(1, size):
        arr.extend(perms(arr[0], num))
        
    return arr

def booleans(s, ops):
    n = len(ops)
    op = {'&': lambda x, y: x & y,
          '|': lambda x, y: x | y,
          '^': lambda x, y: x ^ y}
    s = [True if val == 't' else False for val in s]
    for i in range(n):
        s[i] = [s[i], i, op[ops[i]], s[i+1]]
        
    s.pop()
    tree = dict()
    cms = combs(n)
    for inds in cms:
        del inds[-1]
        fill = tree
        for i in inds:
            if fill.get(i, None) is None:
                fill[i] = dict()
                
            fill = fill[i]
            
    return calc_tree(tree, s)
    
if __name__ == '__main__':
    print(booleans('ttftftft','|&^&^|&'))
