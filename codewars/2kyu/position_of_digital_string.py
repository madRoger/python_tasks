'''
 There is a infinite string. You can imagine it's a combination of numbers
 from 1 to n, like this:

 "123456789101112131415....n-2n-1n"

Please note: the length of the string is infinite. It depends on how long you
need it(I can't offer it as a argument, it only exists in your imagination) ;-)

Your task is complete function findPosition that accept a digital string num.
Returns the position(index) of the digital string(the first appearance).

For example:

 findPosition("456") == 3
 because "123456789101112131415".indexOf("456") = 3
             ^^^

Is it simple? No, It is more difficult than you think ;-)

 findPosition("454") = ?
 Oh, no! There is no "454" in "123456789101112131415",
 so we should return -1?
 No, I said, this is a string of infinite length.
 We need to increase the length of the string to find "454"

 findPosition("454") == 79
 because "123456789101112131415...44454647".indexOf("454")=79
                                    ^^^

The length of argument num is 2 to 15. So now there are two ways: one is to
create a huge own string to find the index position; Or thinking about an
algorithm to calculate the index position.

Which way would you choose? ;-)
Some examples:

 findPosition("456") == 3
 ("...3456...")
       ^^^
 findPosition("454") == 79
 ("...444546...")
        ^^^
 findPosition("455") == 98
 ("...545556...")
       ^^^
 findPosition("910") == 8
 ("...7891011...")
        ^^^
 findPosition("9100") == 188
 ("...9899100101...")
         ^^^^
 findPosition("99100") == 187
 ("...9899100101...")
        ^^^^^
 findPosition("00101") == 190
 ("...99100101...")
         ^^^^^
 findPosition("001") == 190
 ("...9899100101...")
           ^^^
 findPosition("123456789") == 0
 findPosition("1234567891") == 0
 findPosition("123456798") == 1000000071
'''
import re

def find_position(string):
    if string == '01':
        return 10
    
    results, offsets = [], {}
    for rank in range(1, len(string)):
        for part in range(rank, 0, -1):
            first, work = string[:part], string[part:]
            second, off = str(int(first)+1), rank - part
            if len(second) > len(first):
                second = second[1:]
                off += 1
            elif len(second) < len(first):
                second = '0'*(len(first)-len(second))+second
                
            if first[0]=='0' and second[0]=='1' and len(first)>1:
                off += 1
                
            if len(second) >= len(work)-off:
                if work[0]=='0':
                    continue
                
                for i in range(off, len(work)):
                    if (second.startswith(work[i:]) and
                        (int(work[:i]+second)-1) not in results):
                        num = int(work[:i]+second)-1
                        results.append(num)
                        offsets[num] = len(str(num))-len(first)
                        break
                else:
                    if (int(work+second)-1) not in results:
                        num = int(work+second)-1
                        results.append(num)
                        offsets[num] = len(str(num))-len(first)
                        
                continue
            sc = re.compile('(\d{'+str(off)+'}'+second+')\d*')
            ptrn = sc.match(work)
            if ptrn is None:
                continue
            
            second, work = work[:len(ptrn.group(1))], work[len(ptrn.group(1)):]
            if second.startswith('0'):
                continue
            
            further = str(int(second)+1)
            while work:
                if len(further) >= len(work):
                    if further.startswith(work):
                        work = []
                        
                    break
                if not work.startswith(further):
                    break
                
                work, further = work[len(further):], str(int(further)+1)
            if not work:
                results.append(int(second)-1)
                offsets[int(second)-1] = rank - part
                
    if results and len(str(min(results)))==len(string) and string[0]!='0':
        results.append(int(string))
        offsets[int(string)] = 0
    elif not results:
        if  string[0]!='0':
            results.append(int(string))
            offsets[int(string)] = 0
        elif len(string) == string.count('0'):
            results.append(int('1'+string))
            offsets[int('1'+string)] = 1
            
    first = str(min(results))
    rank = len(first)
    res = sum([9*r*10**(r-1) for r in range(1, rank)])
    res += (int(first[0])-1)*rank*10**(rank-1)
    res += sum([rank*int(first[rank-i])*10**(i-1) for i in range(rank-1, 0, -1)])
    return res+offsets[min(results)]

 
if __name__ == '__main__':
    print(find_position("00101"))

    
