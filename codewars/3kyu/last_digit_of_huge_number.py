'''
For a given list [x1, x2, x3, ..., xn] compute the last (decimal)
digit of x1 ^ (x2 ^ (x3 ^ (... ^ xn))).

E. g.,

last_digit([3, 4, 2]) == 1

because 3 ^ (4 ^ 2) = 3 ^ 16 = 43046721.

Beware: powers grow incredibly fast. For example, 9 ^ (9 ^ 9) has more
than 369 millions of digits. lastDigit has to deal with such numbers efficiently.

Corner cases: we assume that 0 ^ 0 = 1 and that lastDigit of an empty list
equals to 1.
'''
def mod_4(num):
    orig, num = num, num % 4
    if num in (0, 1) and orig != num:
        num += 4
        
    return num

def last_digit(lst):
    if not lst:
        return 1
    elif len(lst) == 1:
        return lst[0]%10
    else:
        lst[-1] = mod_4(lst[-1])
        
    for j in reversed(range(1, len(lst)-1)):
        lst[j] = mod_4(lst[j])
        lst[j] = 1 if not lst[j] and not lst[j+1] else lst[j]**lst[j+1]
        lst[j] = mod_4(lst[j])
        
    lst[0] **= lst[1]
    return lst[0]%10

 
if __name__ == '__main__':
    print(last_digit([3, 4, 2]))

    
