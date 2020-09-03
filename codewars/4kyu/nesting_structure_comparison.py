'''
Complete the function/method (depending on the language)
to return true/True when its argument is an array that has
the same nesting structures and same corresponding length of
nested arrays as the first array.

For example:

# should return True
same_structure_as([ 1, 1, 1 ], [ 2, 2, 2 ] )
same_structure_as([ 1, [ 1, 1 ] ], [ 2, [ 2, 2 ] ] )

# should return False 
same_structure_as([ 1, [ 1, 1 ] ], [ [ 2, 2 ], 2 ] )
same_structure_as([ 1, [ 1, 1 ] ], [ [ 2 ], 2 ] )

# should return True
same_structure_as([ [ [ ], [ ] ] ], [ [ [ ], [ ] ] ] )

# should return False
same_structure_as([ [ [ ], [ ] ] ], [ [ 1, 1 ] ] )


'''
def flat_list(s, level=0):
    if not isinstance(s, list):
        return s
    
    result, item = [str(level)+'-0'], 1
    for elem in s:
        if isinstance(elem, list):
            result.extend(flat_list(elem, level+1))
        else:
            result.append('{}-{}'.format(level, item))
            item += 1
            
    return result
    
def same_structure_as(original, other):
    return flat_list(original) == flat_list(other)
 
if __name__ == '__main__':
    print(same_structure_as([1, [1, 1]], [[2, 2], 2]))
    
