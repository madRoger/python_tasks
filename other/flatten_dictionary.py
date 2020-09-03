'''
Given a nested dictionary, flatten the dictionary, where nested
dictionary keys can be represented through dot notation.

Example:

Input: {
  'a': 1,
  'b': {
    'c': 2,
    'd': {
      'e': 3
    }
  }
}
Output: {
  'a': 1,
  'b.c': 2,
  'b.d.e': 3
}
'''
def flatDict(d, parent=''):
    result = {}
    for key, value in d.items():
        if isinstance(value, dict):
            for subKey, subValue in flatDict(value, parent+key+'.').items():
                result[subKey] = subValue
        else:
            result[parent+key] = value
            
    return result

if __name__ == '__main__':
    d = {
        'a': 1,
        'b': {
            'c': 2,
            'd': {
                'e': 3
                },
            'f': {
                'g': 4
                }
            },
        'h': 5
        }

    print(flatDict(d))
