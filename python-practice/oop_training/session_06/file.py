#decorator

def D(func):
    def wrapper():
        print("befor")
        func()
        print("after")
    
    return wrapper

def f():
    print('hello')

x = D(f)
x()

print("\n===================================\n")

def D(func):
    def wrapper():
        print("befor")
        func()
        print("after")
    
    return wrapper 

@D
def f():
    print('hello')

f()

print("\n===================================\n")

def D(func):
    def wrapper():
        print("befor")
        func()
        func()
        print("after")
    
    return wrapper 

@D
def f():
    print('python')

f()

print("\n===================================\n")

def d(func):
    def wrapper(a):
        func(a + 3)
    return wrapper

# @d
def g(x):
    print(x)

g(5)

print('--------------')

def d(func):
    def wrapper(a):
        func(a + 3)
    return wrapper

@d
def g(x):
    print(x)

g(5)

print("\n===================================\n")

"""
instancemethod

    def f(self, a):
        pass

                
classmethod

    @classmethod
    def g(cls, a):
        pass
        

staticmethod

    @staticmethod
    def h(a):
        pass
"""

#instancemethod

class I:
    def __init__(self, a):
        self.a = a
    
    def f(self, i):
        print(self.a)
        return self.a + i
    
ob = I(3)
print(ob.a)
print(ob.f(5))

# print(I.a)
# print(I.f(5))

print('--------------')

#staticmethod

class S:
    def __init__(self, a):
        self.a = a
    
    @staticmethod
    def func_sum(m, n):
        print(m + n)
        # print(self.a)
    
S.func_sum(2, 3)

ob = S(0)
ob.func_sum(2, 3)

print(S.func_sum == ob.func_sum)

print('--------------')

#classmethod

class C:
    def __init__(self, a):
        self.a = a

    @classmethod
    def h(cls, t):
        print(t + 2)
        # print(self.a)
        return cls(t)
    
C.h(10)

ob = C(0)
ob.h(10)

print(C.h == ob.h)

print()
print(ob.h(10))

print()
print(C.h(10).a)


print("\n===================================\n")

from datetime import date

class C:
    def __init__(self, name, age):
        self.name = name 
        self.age = age
    
    @classmethod
    def f(cls, name, year):
        y = date.today().year - year
        return cls(name, y)
    
    @staticmethod
    def s(age):
        if age < 50: 
            return True
        else:
            return False

ob = C.f('Amirreza', 2003)
print(ob.age)
print(ob.name)

print(ob.s(ob.age))
print(C.s(ob.age))

print("\n===================================\n")

class Date:
    def __init__(self, day=0, month=0, year=0):
        self.day = day
        self.month = month
        self.year = year
    
    @classmethod
    def f(cls, s):
        lst = s.split('-')
        return cls(lst[0], lst[1], lst[2])

    @staticmethod
    def g(s):
        day, month, year = map(int, s.split('-'))
        if day <= 31 and day >= 1:
            if month <= 12 and month >= 1:
                return True
            return False
        return False 

ob = Date.f('11-09-2023')
print(ob.year)

v = Date.g('11-09-2023')
print(v)

v = Date.g('11-30-2023')
print(v)

print("\n===================================\n")

class Person:
    def __init__(self, name, family):
        self.name = name
        self.family = family
    
    def f(self):
        return self.name + ' ' + self.family

ob = Person('sara', 'rasti')
print(ob.f) #sara rasti

print('--------------')

class Person:
    def __init__(self, name, family):
        self.name = name
        self.family = family
    
    @property
    def f(self):
        return self.name + ' ' + self.family

ob = Person('sara', 'rasti')
print(ob.f) #sara rasti

print("\n===================================\n")

class Person:
    def __init__(self, name, family):
        self.name = name
        self.family = family
    
    @property
    def f(self):
        return self.name + ' ' + self.family

    @f.setter
    def f(self, s):
        name, family = s.split(' ')
        self.name = name
        self.family = family

ob = Person('sara', 'rasti')
print(ob.f)

ob.f = 'amirreza mehrabani'
print(ob.name)
print(ob.family)

print("\n===================================\n")

class Test:
    # @classmethod
    def f(k):
        return k.__name__
    
    f = classmethod(f)

print(Test.f())

print("\n===================================\n")

class Number:

    a = 3

    def __init__(self, x, y) -> None:
        self.x = x 
        self.y = y

    def add(self):
        return self.x + self.y
    
    @classmethod
    def mul(cls, b):
        return b * cls.a
    
    @staticmethod
    def sub(a, b):
        return a - b  

    @property
    def value(self):
        return(self.x , self.y)
    
    @value.setter
    def value(self, s):
        self.x, self.y = s

    @value.deleter
    def value(self):
        del self.x
        del self.y
    
ob = Number(2, 3)
print(ob.add())
print(ob.mul(4))        
print(ob.sub(3,2))
print(ob.value)
ob.value = (4, 5)
print(ob.value)

print("\n===================================\n")

def d(func):
    def w():
        '''hello'''
        print(func.__name__)
        return func()
    return w
@d
def f(x):
    '''python'''
    return x+2

print(f.__name__)
print(f.__doc__)

print('--------------')

from functools import wraps
def d(func):
    @wraps(func)
    def w():
        '''hello'''
        print(func.__name__)
        return func()
    return w
@d
def f(x):
    '''python'''
    return x+2

print(f.__name__)
print(f.__doc__)

print("\n===================================\n")

class A:
    def __init__(self, a):
        self.a = a

    def f(self):
        return self.a + 2
    
class B(A):
    pass

ob = B(5)
print(ob.f())

print('--------------')

from abc import ABC, abstractmethod

class A:
    def __init__(self, a):
        self.a = a
        super().__init__()

    @abstractmethod
    def f(self):
        pass
    
class B(A):
    def f(self):
        return self.a + 2

ob = B(5)
print(ob.f())

print('--------------')

from abc import ABC, abstractmethod

class A:
    def __init__(self, a):
        self.a = a
        super().__init__()

    @abstractmethod
    def f(self):
        pass
    
class B(A):
    def f(self):
        return self.a + 2
    
class C(A):
    def f(self):
        return self.a ** 2

ob = B(5)
print(ob.f())

ob = C(5)
print(ob.f())