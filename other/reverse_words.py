'''
Given a list of words in a string, reverse the words in-place
(ie don't create a new string and reverse the words).
Since python strings are not mutable, you can assume the input
will be a mutable sequence (like list).
'''
def sort_func():
    c, space = 0, False
    def sort(a):
        nonlocal c, space
        if a == ' ' or space:
            c -= 1
            space = not space
            
        return c
    return sort

def reverse_words(words):
    words.sort(key=sort_func())


if __name__ == '__main__':
    s = list("can you read this")
    reverse_words(s)
    print(''.join(s))
