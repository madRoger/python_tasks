'''
Given a non-empty list of words, return the k most frequent words.
The output should be sorted from highest to lowest frequency, and
if two words have the same frequency, the word with lower alphabetical
order comes first. Input will contain only lower-case letters.

Example:

Input: ["daily", "interview", "pro", "pro", 
"for", "daily", "pro", "problems"], k = 2
Output: ["pro", "daily"]
'''
from collections import Counter

def topKFrequent(words, k):
    words.sort()
    return [word for word, _ in Counter(words).most_common(k)]

if __name__ == '__main__':
    words = ["daily", "interview", "pro", "pro", 
             "for", "daily", "pro", "problems"]
    print(topKFrequent(words, 2))
