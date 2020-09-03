'''
In this kata we want to convert a string into an integer. The strings simply
represent the numbers in words.

Examples:

    "one" => 1
    "twenty" => 20
    "two hundred forty-six" => 246
    "seven hundred eighty-three thousand nine hundred and nineteen" => 783919

Additional Notes:

    The minimum number is "zero" (inclusively)
    The maximum number, which must be supported is 1 million (inclusively)
    The "and" in e.g. "one hundred and twenty-four" is optional, in some cases
    it's present and in others it's not
    All tested numbers are valid, you don't need to validate them
'''
def parse_int(string):
    nums = {'zero': 0, 'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5,
            'six': 6, 'seven': 7, 'eight': 8, 'nine': 9, 'ten': 10, 'eleven': 11,
            'twelve': 12, 'thirteen': 13, 'fourteen': 14, 'fifteen': 15, 'sixteen':16,
            'seventeen': 17, 'eighteen': 18, 'nineteen': 19, 'twenty': 20,
            'thirty': 30, 'forty': 40, 'fifty': 50, 'sixty': 60, 'seventy': 70,
            'eighty': 80, 'ninety': 90 }
    power, result = 1, 0
    for num in reversed(string.split()):
        if num == 'and':
            continue
        
        if num == 'hundred':
            power *= 100
            continue
        
        if num == 'thousand':
            power = 1000
            continue
        
        if num == 'million':
            power = 1000000
            continue
        
        if '-' in num:
            be = num.split('-')
            result += (nums.get(be[0], 0) + nums.get(be[1], 0)) * power
        else:
            result += nums.get(num, 0) * power
            
    return result
 
if __name__ == '__main__':
    print(parse_int("one million twenty hundred forty-six"))
    
