'''
Write a function which makes a list of strings representing all of the ways
you can balance n pairs of parentheses
Examples

balanced_parens(0) => [""]
balanced_parens(1) => ["()"]
balanced_parens(2) => ["()()","(())"]
balanced_parens(3) => ["()()()","(())()","()(())","(()())","((()))"]
'''

def movings(num):
    pools = [tuple(range(n, -1, -1)) for n in range(num-1, 0, -1)]
    result = [[]]
    for pool in pools:
        result = [x+[y] for x in result for y in pool if not x or y<=x[-1]]
        
    for prod in result:
        yield tuple(prod)

def balanced_parens(n):
    result = []
    for steps in movings(n):
        pars = ['(']*n + [')']*n
        for i in range(n-1):
            if steps[i]:
                pars.insert(n-i+steps[i], '(')
                del pars[n-i-1]
                
        result.append(''.join(pars))
        
    return result

 
if __name__ == '__main__':
    print(balanced_parens(3))

    
