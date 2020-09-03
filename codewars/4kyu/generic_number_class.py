'''
Your task in this kata is to implement the function create_number_class which
will take a string parameter alphabet and return a class representing a number
composed of this alphabet.

The class number will implement the four classical arithmetic operations
(+, -, *, //), a method to convert itself to string, and a convert_to method
which will take another class number as parameter and will return the value
of the actual class number converted to the equivalent value with tha alphabet
of the parameter class (return a new instance of this one).

Example:

BinClass = create_number_class('01')
HexClass = create_number_class('0123456789ABCDEF')

x = BinClass('1010')
y = BinClass('10')

print(x+y)                   => '1100'
isinstance(x+y, BinClass)    => True
print(x.convert_to(HexClass) => 'A'

Notes:

    Only positives integers will be used (either as parameters or results of
    calculations).
    You'll never encounter invalid calculations (divisions by zero or things
    like that).
    Alphabets will contain at least 2 characters.


'''
def create_number_class(alphabet):
    class Base:
        base = alphabet
        
        def __init__(self, s):
            if not s:
                raise ValueError("Empty string is incorrect")
            
            for sym in s:
                if sym not in __class__.base:
                    raise ValueError("Incorrect value")
                
            size = len(__class__.base)
            self.value = sum([__class__.base.index(s[-i-1]) * size**i for i in range(len(s))])
            
        def __add__(self, other):
            inst = Base(str(self))
            inst.value = inst.value + other.value
            return inst

        def __iadd__(self, other):
            self.value += other.value
            return self
        
        def __sub__(self, other):
            if other.value > self.value:
                raise ValueError("Result of calculation must be positive or zero")
            
            inst = Base(str(self))
            inst.value = inst.value - other.value
            return inst

        def __isub__(self, other):
            if other.value > self.value:
                raise ValueError("Result of calculation must be positive or zero")
            
            self.value -= other.value
            return self

        def __mul__(self, other):
            inst = Base(str(self))
            inst.value = inst.value * other.value
            return inst

        def __imul__(self, other):
            self.value *= other.value
            return self

        def __floordiv__(self, other):
            inst = Base(str(self))
            inst.value = inst.value // other.value
            return inst

        def __ifloordiv__(self, other):
            self.value //= other.value
            return self
        
        def __str__(self):
            result, num, size = '', self.value, len(__class__.base)
            while num >= size:
                result = __class__.base[num%size] + result
                num //= size
                
            result = __class__.base[num] + result
            return f'{result}'

        def convert_to(self, aClass):
            inst = aClass(aClass.base[0])
            inst.value = self.value
            return inst
        
    return Base

if __name__ == '__main__':
    BinClass = create_number_class('01')
    HexClass = create_number_class('0123456789ABCDEF')

    x = BinClass('1010')
    y = BinClass('10')

    print(x+y)
    print(isinstance(x+y, BinClass))
    print(x.convert_to(HexClass))
