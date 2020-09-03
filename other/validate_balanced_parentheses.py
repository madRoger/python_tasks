'''
Imagine you are building a compiler. Before running any code, the compiler
must check that the parentheses in the program are balanced. Every opening
bracket must have a corresponding closing bracket. We can approximate this
using strings.

Given a string containing just the characters '(', ')', '{', '}', '[' and ']',
determine if the input string is valid.
An input string is valid if:
- Open brackets are closed by the same type of brackets.
- Open brackets are closed in the correct order.
- Note that an empty string is also considered valid.

Example:

Input: "((()))"
Output: True

Input: "[()]{}"
Output: True

Input: "({[)]"
Output: False
'''
def isValid(seq):
    brackets = {'(': 1, ')': -1, '{': 2, '}': -2, '[': 3, ']': -3}
    stack = []
    for br in seq:
        key = brackets.get(br, 0)
        if key == 0:
            print ('Wrong symbol is present')
            return False
        
        if key > 0:
            stack.append(key)
            continue

        if not stack or key + stack.pop() != 0:
            return False

    return not stack

if __name__ == '__main__':
    print (isValid('((()))'))
    print (isValid('[()]{}'))
    print (isValid('({[)]'))
    print (isValid('(([()]{[{}]}))')) 
