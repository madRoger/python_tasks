'''
Given a mathematical expression as a string you must return the result as a number.
Numbers

Number may be both whole numbers and/or decimal numbers. The same goes for the
returned result.
Operators

You need to support the following mathematical operators:

    Multiplication *
    Division / (as true division)
    Addition +
    Subtraction -

Operators are always evaluated from left-to-right, and * and / must be evaluated
before + and -.
Parentheses

You need to support multiple levels of nested parentheses, ex. (2 / (2 + 3.33) * 4) - -6
Whitespace

There may or may not be whitespace between numbers and operators.

An addition to this rule is that the minus sign (-) used for negating numbers and
parentheses will never be separated by whitespace. I.e., all of the following are valid
expressions.

1-1    // 0
1 -1   // 0
1- 1   // 0
1 - 1  // 0
1- -1  // 2
1 - -1 // 2

6 + -(4)   // 2
6 + -( -4) // 10

And the following are invalid expressions

1 - - 1    // Invalid
1- - 1     // Invalid
6 + - (4)  // Invalid
6 + -(- 4) // Invalid

Validation

You do not need to worry about validation - you will only receive valid mathematical
expressions following the above rules.

NOTE: eval and exec are disallowed in your solution.
'''
import re

def sub_calc(data):
    prm_ops = {'*': lambda x, y: x*y, '/': lambda x, y: x/y,}
    ops = {'+': lambda x, y: x+y, '-': lambda x, y: x-y,}
    ops.update(prm_ops)
    clc = []
    while True:
        for i in range(1, len(data)):
            if data[i] in ops:
                num = data[:i]
                if data[i-1] != '-':
                    clc.append(float(num) if '.' in num else int(num))
                    clc.append(ops[data[i]])
                    
                data = data[i+1:]
                break
        else:
            clc.append(float(data) if '.' in data else int(data))
            break
    while True:
        for i in range(1, len(clc), 2):
            if clc[i] in prm_ops.values():
                clc[i+1] = clc[i](clc[i-1], clc[i+1])
                clc = clc[:i-1] + clc[i+1:]
                break
        else:
            break
    for i in range(1, len(clc), 2):
        clc[i+1] = clc[i](clc[i-1], clc[i+1])
        
    return clc[-1]

def calc(expression):
    expression = ''.join([sym for sym in expression if sym != ' '])
    block = re.compile('\([^()]+\)')
    part = block.search(expression)
    while part is not None:
        result = str(sub_calc(expression[part.start()+1:part.end()-1]))
        expression = expression[:part.start()]+result+expression[part.end():]
        part = block.search(expression)
        
    return sub_calc(expression)

 
if __name__ == '__main__':
    print(calc('6 + -( -4)'))

    
