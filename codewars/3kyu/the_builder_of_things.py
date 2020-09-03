'''
Examples of what can be done with "Thing":

jane = Thing('Jane')
jane.name # => 'Jane'

# can define boolean methods on an instance
jane.is_a.person
jane.is_a.woman
jane.is_not_a.man

jane.is_a_person # => True
jane.is_a_man # => False

# can define properties on a per instance level
jane.is_the.parent_of.joe
jane.parent_of # => 'joe'

# can define number of child things
# when more than 1, a tuple subclass is created
jane.has(2).legs
len(jane.legs) # => 2
isinstance(jane.legs[0], Thing) # => True

# can define single items
jane.has(1).head
isinstance(jane.head, Thing) # => True

# can define number of things in a chainable and natural format
>> Note: Python, unlike Ruby and Javascript, doesn't have a pretty syntax for
blocks of expressions and a forEach method for iterables. So you should
implement this behaviour yourself.
jane.has(2).arms.each.having(1).hand.having(5).fingers
len(jane.arms[0].hand.fingers) # => 5

# can define properties on nested items
jane.has(1).head.having(2).eyes.each.being_the.color.blue.having(1).pupil.being_the.color.black

# can define methods: thing.can.verb(method, past='')
method = lambda phrase: "%s says: %s" % (name, phrase)
# or 
def method(phrase):
  return "%s says: %s" % (name, phrase)
jane.can.speak(method, "spoke")

jane.speak("hello") # => "Jane says: hello"

# if past tense was provided then method calls are tracked
jane.spoke # => ["Jane says: hello"]
Note: Most of the test cases have already been provided for you so that you can
see how the Thing object is supposed to work.
'''
from collections import defaultdict

class Thing:
    
    def __init__(self, name=None):
        self.name = name
        self.whos = set()
        self.roles = defaultdict(list)
        
        self.is_a = Is_a(self)
        self.is_not_a = Is_not_a(self)
        self.is_the = Is_the(self)
        self.can = Can(self)

    def has(self, size):
        return Has(size, self)
    
    def having(self, size):
        return self.has(size)
    
class Is:

    def __init__(self, owner):
        self.owner = owner

    def __getattr__(self, name):
        if not hasattr(Thing, 'is_a_'+name):
            setattr(Thing, 'is_a_'+name, IsaCheck(name))
            
        if not hasattr(Thing, 'is_not_a_'+name):
            setattr(Thing, 'is_not_a_'+name, IsNotaCheck(name))

class Is_a(Is):
    
    def __getattr__(self, name):
        if name not in self.owner.whos:
            self.owner.whos.add(name)
            
        super().__getattr__(name)    

class Is_not_a(Is):
    
    def __getattr__(self, name):
        if name in self.owner.whos:
            self.owner.whos.remove(name)
            
        super().__getattr__(name)

class Is_the(Is):

    def __getattr__(self, name):
        self.owner.roles[name].append(Relative())
        if not hasattr(Thing, name):
            setattr(Thing, name, IsTheCheck(name))
        return self.owner.roles[name][-1]

class Relative:
    
    def __getattr__(self, name):
        setattr(self, 'name', name)
        
class IsCheck:
    def __init__(self, status):
        self.status = status
            
    def __get__(self, instance, owner):
        pass
    
class IsaCheck(IsCheck):
    
    def __get__(self, instance, owner):
        return self.status in instance.whos
    
class IsNotaCheck(IsCheck):
    
    def __get__(self, instance, owner):
        return self.status not in instance.whos

class IsTheCheck(IsCheck):
    
    def __get__(self, instance, owner):
        return ', '.join([body.name for body in instance.roles[self.status]])

class Has:

    def __init__(self, size, owner):
        self.size = size
        self.owner = owner

    def __getattr__(self, name):
        if hasattr(self.owner, name):
            attr = getattr(self.owner, name)
            if isinstance(attr, Thing) and self.size > 1:
                raise ValueError
            
            if isinstance(attr, Things) and self.size != len(attr):
                raise ValueError
            
            return attr
        
        thing_name = name[:-1] if name.endswith('s') else name
        if self.size > 1:
            things = Things([Thing(thing_name)]*self.size)
            for thing in things:
                setattr(thing, 'is_'+thing_name, True)
                
            setattr(self.owner, name, things)
        else:
            thing = Thing(name)
            setattr(thing, 'is_'+thing_name, True)
            setattr(self.owner, name, thing)
        return getattr(self.owner, name)

class Can:

    def __init__(self, owner):
        self.owner = owner
        
    def create(self, *args):
        if not args:
            return
        
        args[0].__globals__['name'] = self.owner.name
        if len(args)==1:
            setattr(self.owner, self.method_name, args[0])
        else:
            setattr(self.owner, args[-1], [])
            def logged(func):
                log = getattr(self.owner, args[-1])
                def wrapper(*args):
                    result = func(*args)
                    log.append(result)
                    return result
                
                return wrapper
            setattr(self.owner, self.method_name, logged(args[0]))
        
    def __getattr__(self, name):
        self.method_name = name
        return self.create
        
class Things(tuple):

    def __init__(self, data):
        self.each = self
        self.being_the = PropertyThingsIterator(self)
        self.and_the = PropertyThingsIterator(self)

    def having(self, size):
        return ThingsIterator(self, size)
    
class ThingsIterator:
    
    def __init__(self, data, size):
        self.data = data
        self.size = size

    def __getattr__(self, name):
        for part in self.data:
            thing_name = name[:-1] if name.endswith('s') else name
            if self.size > 1:
                things = Things([Thing(thing_name)]*self.size)
                for thing in things:
                    setattr(thing, 'is_'+thing_name, True)
                    
                setattr(part, name, things)
            else:
                thing = Thing(name)
                setattr(thing, 'is_'+thing_name, True)
                setattr(part, name, thing)
                
        return Things([getattr(p, name) for p in self.data])

class PropertyThingsIterator:
    
    def __init__(self, data):
        self.data = data
        self.mode = 'WAIT_ATTR'

    def __getattr__(self, name):
        if self.mode == 'WAIT_ATTR':
            self.attr = name
            self.mode = 'WAIT_VALUE'
            return self
        
        if self.mode == 'WAIT_VALUE':
            for part in self.data:
                setattr(part, self.attr, name)
                
            return self.data

 
if __name__ == '__main__':
    jane = Thing('Jane')
    print(jane.name)
    
    jane.is_a.person
    jane.is_a.woman
    jane.is_not_a.man

    print('Is a person:', jane.is_a_person)
    print('Is a man:', jane.is_a_man)

    jane.is_the.parent_of.joe
    print('Jane parent of:', jane.parent_of)

    jane.has(2).legs
    print('Jane has', len(jane.legs), 'legs')
    print('Jane has legs:', isinstance(jane.legs[0], Thing))

    jane.has(1).head
    print('Jane has head:', isinstance(jane.head, Thing))

    jane.has(2).arms.each.having(1).hand.having(5).fingers
    print('Jane has', len(jane.arms[0].hand.fingers), 'fingers on each hand')

    jane.has(1).head.having(2).eyes.each.being_the.color.blue.having(1).pupil.being_the.color.black
          
    method = lambda phrase: "%s says: %s" % (name, phrase)
    jane.can.speak(method, "spoke")
    print(jane.speak("hello"))
    print(jane.spoke)
