'''
Given a 32 bit integer, reverse the bits and return that number.

Example:

Input: 1234 
# In bits this would be 0000 0000 0000 0000 0000 0100 1101 0010
Output: 1260388352
# Reversed bits is 0100 1011 0010 0000 0000 0000 0000 0000
'''

def to_bits(n):
    return '{0:08b}'.format(n)

def reverse_num_bits(num):
    return int(bin(num)[2:].zfill(32)[::-1], 2)

if __name__ == '__main__':
    print(to_bits(1234))
    print(reverse_num_bits(1234))
    print(to_bits(reverse_num_bits(1234)))
