'''
Given a positive integer, find the square root of the integer without
using any built in square root or power functions
(math.sqrt or the ** operator). Give accuracy up to 3 decimal points.
'''
def sqrt(x):
    guess, result = x, x - 1
    while guess-result > 0.001:
        guess = result
        result = (guess + (x / guess)) / 2
        
    return '{:.3f}'.format(result)

if __name__ == '__main__':
    print(sqrt(5))
