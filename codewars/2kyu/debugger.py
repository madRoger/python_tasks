'''
Imagine you have a large project where is suddenly going something very messy.
You are not able to guess what it is and don't want to debug all the code
through. Your project has one base class.

In this kata you will write metaclass Meta for your base class, which will
collect data about all attribute accesses and method calls in all project classes.
From this data you can then better guess what is happening or which method call
is bottleneck of your app.

We will use class Debugger to store the data. Method call collection should
look like this:

Debugger.method_calls.append({
    'class': ..., # class object, not string
    'method': ..., # method name, string
    'args': args, # all args, including self
    'kwargs': kwargs
})

Attribute access collection should look like this:

Debugger.attribute_accesses.append({
    'action': 'set', # set/get
    'class': ..., # class object, not string
    'attribute': ..., # name of attribute, string
    'value': value # actual value
})

You should NOT log calls of getter/setter methods that you might create by meta class.
'''
from types import FunctionType

class Debugger(object):
    attribute_accesses = []
    method_calls = []

def get_func(*args):
    value = object.__getattribute__(*args)
    Debugger.attribute_accesses.append({'action': 'get', 'class': args[0],
                                        'attribute': args[1], 'value':value})
    return value

def set_func(*args):
    Debugger.attribute_accesses.append({'action': 'set', 'class': args[0],
                                        'attribute': args[1], 'value':args[2]})
    return object.__setattr__(*args)

def call_decorator(func):
    def call_func(*args, **kwargs):
        Debugger.method_calls.append({'class': args[0], 'method': func.__name__,
                                      'args': args, 'kwargs': kwargs})
        return func(*args, **kwargs)
    return call_func

class Meta(type):
    def __new__(meta, classname, supers, classdict):
        cls = type.__new__(meta, classname, supers, classdict)
        for attr in dir(cls):
            if attr in ('__getattribute__', '__setattr__'):
                continue
            if isinstance(getattr(cls, attr), FunctionType):
                setattr(cls, attr, call_decorator(getattr(cls, attr)))

        cls.__getattribute__ = get_func
        cls.__setattr__ = set_func
        return cls

 
if __name__ == '__main__':
    class Foo(object, metaclass=Meta):

        def __init__(self, x):
            self.x = x

        def bar(self, v):
            return (self.x, v)

    a = Foo(1)
    a.bar(2)

    calls = Debugger.method_calls

    print(len(calls))
    print(calls[0]['args'][-1])
    print(calls[1]['args'][-1])
    accesses = Debugger.attribute_accesses
    print(len(accesses))
    print(accesses[0]['action'])
    print(accesses[0]['attribute'])
    print(accesses[0]['value'])
    print(accesses[1]['action'])
    print(accesses[1]['attribute'])
    print(accesses[2]['action'])
    print(accesses[2]['attribute'])

    
