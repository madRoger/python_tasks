'''
Django is a famous back-end framework written in Python. It has a vast list of
features including the creation of database tables through "models". You can
see an example of such model below:

class Person(models.Model):
    first_name = models.CharField()
    last_name = models.CharField()

Apart from creating a table it can perform validation, generate HTML forms, and
so on. This is possible thanks to metaclasses. Normally there are better solutions
than using metaclasses, but they can be of great help in creating powerful
framework interfaces. This goal of this kata is to learn and understand how such
frameworks works.

Your task is to implement a class Model and classes for its fields to support
functionality like in the following example:

class User(Model):
    first_name = CharField(max_length=30)
    last_name = CharField(max_length=50)
    email = EmailField()
    is_verified = BooleanField(default=False)
    date_joined = DateTimeField(auto_now=True)
    age = IntegerField(min_value=5, max_value=120, blank=True)


user1 = User(first_name='Liam', last_name='Smith', email='liam@example.com')
user1.validate()

print(user1.date_joined)  # prints date and time when the instance was created
print(user1.is_verified)  # prints False (default value)

user1.age = 256
user1.validate()  # raises ValidationError - age is out of range

user2 = User()
user2.validate()  # raises ValidationError - first three fields are missing and
mandatory

The classes which inherit from Model should:

    support creation of fields using class-attribute syntax
    have a validate method which checks whether all fields are valid

The field types which you should implement are:

    CharField - a string with min_length (default 0) and max_length (default None) parameters
    IntegerField - an integer with min_value (default None) and max_value (default None) parameters
    BooleanField - a boolean
    DateTimeField - a datetime with auto_now (default False) parameters which determines
    whether the current time should be set automatically on creation
    EmailField - a string in the format of address@subdomain.domain where address,
    subdomain, and domain are sequences of alphabetical characters with min_length (
    default 0) and max_length (default None) parameters

Also, each field type has parameters blank (default False) which determines whether
None is allowed as a value, and default (default None) which determines the value to
be used if nothing was provided.

Each field type should have its own validate method which checks whether the provided
value has the correct type and satisfies the length/value constraints.
Notes

    min_value/max_value and min_length/max_length bounds are inclusive
    if DateTimeField's auto_now flag is set to True, and no default value is specified,
    accessing its default attribute should always yield current time.

'''
from copy import copy
from datetime import datetime
from re import fullmatch as emailcheck

class ValidationError(Exception):
    pass

class Field:

    def __init__(self, min_length=0, max_length=None, min_value=None,
                 max_value=None, blank=False, default=None):
        self.min_length = min_length
        self.max_length = max_length
        self.min_value = min_value
        self.max_value = max_value
        self.blank = blank
        self.default = default
        self.value = None
        self.name = None

    def get_value(self):
        if self.value is not None or self.blank:
            return self.value
        
        return self.default
        
    def set_value(self, value):
        self.value = value

    def validate(self):
        if not hasattr(self, 'val_type'):
            raise ValidationError(f'{self.name} have incorrect field type')
            
        if (not self.blank and
            self.value is None and
            self.default is None):
            raise ValidationError(f'{self.name} must have (default) value')

        if self.value is not None and not isinstance(self.value, self.val_type):
            raise ValidationError(f'{self.name} must be {self.val_type_name}')
    
class CharField(Field):
    val_type = str
    val_type_name = 'string'
    
    def validate(self):
        super().validate()
        if self.min_length < 0:
            raise ValidationError(f'{self.name}: incorrect min_length')

        if (self.max_length is not None and
            self.min_length > self.max_length):
            raise ValidationError(f'{self.name}: incorrect length range')

        if isinstance(self.value, str):
            if (self.max_length is not None and
                len(self.value) > self.max_length):
                raise ValidationError(f'{self.name}: length is greater than max_length')

            if len(self.value) < self.min_length:
                raise ValidationError(f'{self.name}: length is less than min_length')

class IntegerField(Field):
    val_type = int
    val_type_name = 'integer'
    
    def validate(self):
        super().validate()
        if (self.min_value is not None and
            self.max_value is not None and
            self.min_value > self.max_value):
            raise ValidationError(f'{self.name}: incorrect range')

        if self.value is not None:
            if self.min_value is not None and self.value < self.min_value:
                raise ValidationError(f'{self.name} is less than min_value')

            if self.max_value is not None and self.value > self.max_value:
                raise ValidationError(f'{self.name} is greater than max_value')

class BooleanField(Field):
    val_type = bool
    val_type_name = 'boolean'

from time import sleep
class DateTimeField(Field):
    val_type = datetime
    val_type_name = 'datetime'
    
    def __init__(self, auto_now=False, **kwargs):
        self.auto_now = auto_now
        super().__init__(**kwargs)

    def get_value(self):
        if self.value is not None or self.blank:
            return self.value
        
        if self.default is not None:
            return self.default
        
        if self.auto_now:
            return datetime.now()
        
        return None

    def validate(self):
        if self.value is not None and not isinstance(self.value, self.val_type):
            raise ValidationError(f'{self.name} must be {self.val_type_name}')

class EmailField(CharField):
    
    def validate(self):
        super().validate()
        if self.value is not None:
            if emailcheck('[a-zA-Z]+@[a-zA-Z]+\.[a-zA-Z]+', self.value) is None:
                raise ValidationError(f'{self.name} have incorrect format')
        elif self.default is not None:
            if emailcheck('[a-zA-Z]+@[a-zA-Z]+\.[a-zA-Z]+', self.default) is None:
                raise ValidationError(f'{self.name} default have incorrect format')

class Model:

    fields = dict()
    def __init__(self, **kwargs):
        for cls in self.__class__.__mro__:
            if cls is Model:
                break
            
            for attr, obj in Model.fields.get(cls, dict()).items():
                if attr in self.__dict__:
                    continue
                
                new_obj = copy(obj)
                new_obj.name = attr
                new_obj.value = kwargs.get(attr, None)
                self.__dict__[attr] = new_obj
        
    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        Model.fields[cls] = dict()
        attrfordel = []
        for attr, obj in cls.__dict__.items():
            if isinstance(obj, Field):
                Model.fields[cls][attr] = obj
                attrfordel.append(attr)
                
        for del_attr in attrfordel:
            delattr(cls, del_attr)

    def __getattribute__(self, name):
        obj = object.__getattribute__(self, name)
        return obj.get_value() if isinstance(obj, Field) else obj

    def __setattr__(self, name, value):
        obj = object.__getattribute__(self, name)
        if isinstance(obj, Field):
            obj.set_value(value)
        else:
            object.__setattr__(self, name, value)

    def validate(self):
        for obj in self.__dict__.values():
            if isinstance(obj, Field):
                obj.validate()
                
class User(Model):
        first_name = CharField(max_length=30, default='Adam')
        last_name = CharField(max_length=50)
        email = EmailField()
        is_verified = BooleanField(default=False)
        date_joined = DateTimeField(default=datetime.now())
        age = IntegerField(min_value=5, max_value=120, blank=True)

if __name__ == '__main__':
    class User(Model):
        first_name = CharField(max_length=30)
        last_name = CharField(max_length=50)
        email = EmailField()
        is_verified = BooleanField(default=False)
        date_joined = DateTimeField(auto_now=True)
        age = IntegerField(min_value=5, max_value=120, blank=True)

        user1 = User(first_name='Liam', last_name='Smith', email='liam@example.com')
        user1.validate()

        print(user1.date_joined)
        print(user1.is_verified)

        user1.age = 256
        user1.validate()

        user2 = User()
        user2.validate()


