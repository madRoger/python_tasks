'''
Your function will receive two strings, each comprised of digits representing
a positive integer. These two values will represent the upper and lower bounds
of a range.
Output:

Your function must return the number of valid upside down numbers within the
range of the two input arguments, including both upper and lower bounds.
What is an Upside-Down Number?

An upside down number is an integer that appears the same when rotated 180
degrees, as illustrated below.

Example:

x = '0'
y = '25'
upsidedown(x,y) #4
# the valid numbers in the range are 0, 1, 8, and 11

Additional Notes:

    All inputs will be valid.
    The first argument will always be less than the second argument
    (ie. the range will always be valid).

'''
def incdec(num, digits, direct):
    edgeind = -1 if direct > 0 else 0
    newind = -1 - edgeind
    for i in reversed(range(len(num))):
        if num[i] == digits[edgeind]:
            num[i] = digits[newind]
        else:
            num[i] = digits[digits.index(num[i])+direct]
            break
    
def clamp(num, forward=False):
    if int(num) < 12:
        first4, dnum = [0, 1, 8, 11], int(num)
        if dnum in first4:
            return num
        
        first4.append(dnum)
        first4.sort()
        return str(first4[first4.index(dnum) + (1 if forward else -1)])
    
    digs, middle = ('0', '1', '6', '8', '9'), ('0', '1', '8')
    revdigs = {'0': '0', '1': '1', '6': '9', '8': '8', '9': '6'}
    half = list(num[:len(num)//2])
    mid = num[len(num)//2] if len(num)%2 else ''
    half2 = list(num[len(mid)+len(num)//2:])
#first half
    for i in range(len(half)):
        if half[i] not in digs:
            offset = 0 if forward else -1
            half[i] = digs[sorted(digs+tuple(half[i])).index(half[i])+offset]
            if i < len(half)-1:
                half[i+1:] = [digs[offset]]*(len(half)-i-1)
                
            if mid:
                mid = middle[offset]
                
            half2 = [revdigs[dig] for dig in half[::-1]]
            break
#middle
    if mid and mid not in middle:
        if forward:
            if mid == '9':
                incdec(half, digs, 1)
                
            mid = middle[0 if mid == '9' else -1]
            if half.count('0') == len(half):
                    half, mid = ['1'] + half, ''
        else:
            mid = middle[-1 if mid == '9' else 1]
            
        half2 = [revdigs[dig] for dig in half[::-1]]
#second half
    goodhalf = [revdigs[dig] for dig in half[::-1]]
    if half2 != goodhalf:
        if forward and goodhalf < half2:
            if mid == middle[-1]:
                mid = middle[0]
                incdec(half, digs, 1)
                if half.count('0') == len(half):
                    half, mid = ['1'] + half, ''
            elif mid:
                mid = middle[middle.index(mid)+1]
            else:
                incdec(half, digs, 1)
                if half.count('0') == len(half):
                    half[0], mid = '1', '0'
        elif not forward and goodhalf > half2:
            if mid == middle[0]:
                mid = middle[-1]
                incdec(half, digs, -1)
                if half[0] == '0':
                    half, mid = half[1:] + ['9'], ''
            elif mid:
                mid = middle[middle.index(mid)-1]
            else:
                incdec(half, digs, -1)
                if half[0] == digs[0]:
                    half, mid = half[1:], middle[-1]
                    
        half2 = [revdigs[dig] for dig in half[::-1]]
        
    return ''.join(half) + mid + ''.join(half2)

def index_number(num):
    first7 = ('0', '1', '8', '11', '69', '88', '96')
    if num in first7:
        return first7.index(num) + 1
    
    digs, middle = ('0', '1', '6', '8', '9'), ('0', '1', '8')
    half = list(num[:len(num)//2])
    mid = num[len(num)//2] if len(num)%2 else ''
    head = (digs.index(half[0])-1) * 5**(len(half)-1)
    head += sum([digs.index(d)*5**(len(half)-p) for p, d in enumerate(half[1:-1], 2)])
    tail = 0 if len(half) == 1 else digs.index(half[-1])+int(len(mid)==0)
    midcoeff = 3 if mid else 1
    midoffset = 0 if not mid else middle.index(mid)+1
    offset = (head + tail) * midcoeff + midoffset
    result = sum([12 * 5**pw for pw, _ in enumerate(range(3, len(num), 2))])
    result += sum([4 * 5**pw for pw, _ in enumerate(range(2, len(num), 2))])
    return 3 + result + offset #3 - (0 1 8)

def upsidedown(x,y):
    return index_number(clamp(y, False)) - index_number(clamp(x, True)) + 1

 
if __name__ == '__main__':
    print(upsidedown('0', '25'))

    
