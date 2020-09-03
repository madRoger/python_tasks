'''
Given an integer, check if that integer is a palindrome.
For this problem do not convert the integer to a string
to check if it is a palindrome.
'''

def is_palindrome(n):
    n = abs(n)
    if n < 10:
        return True
    
    workN, power, counter = n, 1, 0
    while n > power:
        power *= 10
        counter += 1
        
    power //= 10
    counter -= counter % 2
    counter //= 2
    for mult in range(counter):
        workN -= (n // power) % 10 * (10 ** mult)
        if workN%(10 ** (mult + 1)):
            return False
        
        power //= 10
        
    return True

if __name__ == '__main__':
    print(is_palindrome(909))
    print(is_palindrome(1234322))
