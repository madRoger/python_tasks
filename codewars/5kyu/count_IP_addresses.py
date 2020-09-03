'''
Implement a function that receives two IPv4 addresses, and returns the
number of addresses between them (including the first one, excluding the
last one).

All inputs will be valid IPv4 addresses in the form of strings. The last
address will always be greater than the first one.
Examples

ips_between("10.0.0.0", "10.0.0.50")  ==   50 
ips_between("10.0.0.0", "10.0.1.0")   ==  256 
ips_between("20.0.0.10", "20.0.1.0")  ==  246
'''
def ips_between(start, end):
    start_octs = start.split('.')[::-1]
    end_octs = end.split('.')[::-1]
    result = 0
    for i in range(4):
        result += (int(end_octs[i])-int(start_octs[i])) * 2**(8*i)
        
    return result
 
if __name__ == '__main__':
    print(ips_between("10.0.0.0", "10.0.0.50"))
    print(ips_between("10.0.0.0", "10.0.1.0"))
    
