'''
Write a class decorator @remember which makes the class remember its own objects,
storing them in a dictionary with the creating arguments as keys.

Also, you have to avoid creating a new member of the class with the same initial
arguments as a previously remembered member.

Additionally, if the (decorated) class is A, you will have to reach that dictionary
of remembered objects directly on A, i.e. by A[args] and by the loop for x in A over the keys.
Example

A sample usage:

@remember
class A(object):
  def __init__(self, x,y=0,z=0):
    pass

a = A(1)
b = A(2,3)
c = A(4,5,6)
d = A(1)

>>> A[1] is a is d
True
>>> A[2,3] is b
True
>>> A[4,5,6] is c
True
>>> for x in A: print x,
(2,3) (4,5,6) 1

Notes.

    Other dict methods like items(), keys(), etc. are nice to have but not
    required to be implemented on the decorated class itself for this kata.
    You don't have to deal with named arguments at creating an instance of
    your class (such as z in A(1,z=5)).
    If the constructor is called with a single argument, the argument itself
    will be the key and not its 1-tuple.


'''
class remember:
    
    def __init__(self, cls):
        self.cls = cls
        self.storage = dict()

    def __call__(self, *args):
        if len(args) == 1:
            args = args[0]
            
        if args not in self.storage:
            if isinstance(args, tuple):
                self.storage[args] = self.cls(*args)
            else:
                self.storage[args] = self.cls(args)
                
        return self.storage[args]

    def __iter__(self):
        return iter(self.storage)

    def __getitem__(self, index):
        return self.storage.get(index, None)

    def keys(self):
        return self.storage.keys()

    def items(self):
        return self.storage.items()
 
if __name__ == '__main__':
    @remember
    class A(object):
        
        def __init__(self, x,y=0,z=0):
            pass

    a = A(1)
    b = A(2,3)
    c = A(4,5,6)
    d = A(1)

    print(A[1] is a is d)
    print(A[2,3] is b)
    print(A[4,5,6] is c)
    for x in A:
        print(x)
    
