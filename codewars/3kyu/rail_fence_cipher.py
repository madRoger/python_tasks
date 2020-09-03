'''
Create two functions to encode and then decode a string using the Rail Fence
Cipher. This cipher is used to encode a string by placing each character
successively in a diagonal along a set of "rails". First start off moving
diagonally and down. When you reach the bottom, reverse direction and move
diagonally and up until you reach the top rail. Continue until you reach the
end of the string. Each "rail" is then read left to right to derive the encoded
string.

For example, the string "WEAREDISCOVEREDFLEEATONCE" could be represented in a
three rail system as follows:

W       E       C       R       L       T       E
  E   R   D   S   O   E   E   F   E   A   O   C  
    A       I       V       D       E       N    

The encoded string would be:
WECRLTEERDSOEEFEAOCAIVDEN

Write a function/method that takes 2 arguments, a string and the number of rails,
and returns the ENCODED string.

Write a second function/method that takes 2 arguments, an encoded string and the
number of rails, and returns the DECODED string.

For both encoding and decoding, assume number of rails >= 2 and that passing an
empty string will return an empty string.

Note that the example above excludes the punctuation and spaces just for simplicity.
There are, however, tests that include punctuation. Don't filter out punctuation as
they are a part of the string.

'''
def encode_rail_fence_cipher(string, n):
    if n < 2 or not string:
        return string
    
    rails, ind, direct = ['']*n, 0, -1
    for sym in string:
        rails[ind] += sym
        if ind == n-1 or not ind:
            direct = -direct
            
        ind += direct
        
    return ''.join(rails)
    
def decode_rail_fence_cipher(string, n):
    if n < 2 or not string:
        return string
    
    size = len(string)
    period = (n - 1) * 2
    topsize = (size-1)//period + 1
    vcount = topsize - 1
    bottomsize = topsize if size-vcount*period >= n else topsize-1
    tailsize = (size-1) - vcount*period
    rails = ['']*n
    rails[0] = string[:topsize]
    if bottomsize:
        rails[-1] = string[-bottomsize:]
        
    string = string[topsize:-bottomsize] if bottomsize else string[topsize:]
    for i in range(n-2):
        rails[i+1] += string[:vcount*2]
        string = string[vcount*2:]
        if (n-2)*2-i < tailsize:
            rails[i+1] += string[:2]
            string = string[2:]
        elif i < tailsize:
            rails[i+1] += string[0]
            string = string[1:]
            
    result, ind, direct = '', 0, -1
    while size:
        result += rails[ind][0]
        rails[ind] = rails[ind][1:]
        if ind == n-1 or not ind:
            direct = -direct
            
        ind += direct
        size -= 1
        
    return result

 
if __name__ == '__main__':
    print(encode_rail_fence_cipher("WEAREDISCOVEREDFLEEATONCE", 3))
    print(decode_rail_fence_cipher(encode_rail_fence_cipher("WEAREDISCOVEREDFLEEATONCE", 3), 3))
    
