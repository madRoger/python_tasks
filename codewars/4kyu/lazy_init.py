'''
How many times we create a python class and in the init method we just write:

self.name1 = name1
self.name2 = name2
.....

for all arguments.....

How boring!!!!

Your task here is to implement a metaclass that let this instantiation be done
automatically. But let's see an example:

class Person(metaclass=LazyInit):
  def __init__(self, name, age): pass

When we create a Person object like:

a_person = Person('John', 25)

The expected behavior will be:

print(a_person.name) # this will print John
print(a_person.age)  # this will print 25

Obviously the number of arguments might be different from class to class.
Don't worry about **kwargs you will never be given keyword arguments in this
kata!!!
A little hint: a decorator could help you out doing the job!!!
'''
def LazyInit(className, supers, classDict):
    aClass = type(className, supers, classDict)

    class Wrapper:

        def __init__(self, *args):
            instance = aClass(*args)
            code = instance.__init__.__code__
            argNames = code.co_varnames[1:code.co_argcount]
            instance.__dict__.update(zip(argNames, args))
            self.wrapped = instance

        def __getattr__(self, name):
            return getattr(self.wrapped, name)

    return Wrapper
 
if __name__ == '__main__':
    class Person(metaclass=LazyInit):
        
        def __init__(self, name, age): pass

    a_person = Person('John', 25)
    print(a_person.name)
    print(a_person.age)
