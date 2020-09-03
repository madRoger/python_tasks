'''
Input
    Range is 0-999
    There may be duplicates
    The array may be empty
Example
    Input: 1, 2, 3, 4
    Equivalent names: "one", "two", "three", "four"
    Sorted by name: "four", "one", "three", "two"
    Output: 4, 1, 3, 2
Notes
    Don't pack words together:
        e.g. 99 may be "ninety nine" or "ninety-nine"; but not "ninetynine"
        e.g 101 may be "one hundred one" or "one hundred and one"; but not "onehundredone"
    Don't fret about formatting rules, because if rules are consistently applied it has no effect anyway:
        e.g. "one hundred one", "one hundred two"; is same order as "one hundred and one", "one hundred and two"
        e.g. "ninety eight", "ninety nine"; is same order as "ninety-eight", "ninety-nine"

'''
def num_in_latters(num):
    if not -1 < num < 1000:
        return 'zz'
    
    lower20 = ['zero', 'one', 'two', 'three' ,'four', 'five', 'six', 'seven',
              'eight', 'nine', 'ten', 'eleven', 'twelve', 'thirteen', 'fourteen',
              'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen']
    if num < 20:
        return lower20[num]
    
    lower20[0] = ''
    dozens = ['', '', 'twenty', 'thirty', 'forty', 'fifty',
              'sixty', 'seventy', 'eighty', 'ninety']
    result = ''
    hund = num // 100
    dozen = num % 100
    if hund:
        if dozen:
            result += lower20[hund] + ' hundred and '
        else:
            return lower20[hund] + ' hundred'
        
    if dozen < 20:
        result += lower20[dozen]
    else:
        result += dozens[dozen//10] + ' ' + lower20[dozen%10]
        
    return result

def sort_by_name(arr):
    return sorted(arr, key=num_in_latters)
 
if __name__ == '__main__':
    print(sort_by_name([1, 2, 3, 4, 5]))
    
