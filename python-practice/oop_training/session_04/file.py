'''
dunder in class : double underscore

__init__
__str__
__len__
__getitem__
__setitem__
__repr__
__call__

#overload
__add__
__gt__  greater than
__lt__  less than
__eq__  equal


__set__
__get__
'''

class Test:
    def __init__(self):
        self.lst = [12, 3, 4]

ob = Test()

print(ob) #<__main__.Test object at 0x7f846068c0d0>
print(ob.lst)

print('-------------------------------------')

class Test:
    def __init__(self):
        self.lst = [12, 3, 4]

    def __str__(self):
        return str(self.lst)

ob = Test()

print(ob)
print(ob.lst)
# print(len(ob))

print('-------------------------------------')

class Test:
    def __init__(self):
        self.lst = [12, 3, 4]

    def __str__(self):
        return str(self.lst)
    
    # def __len__(self):
    #     return len(self.lst)

print(ob)
print(ob.lst)
# print(len(ob)) TypeError: object of type 'Test' has no len() ?????????

print('-------------------------------------')

class Test:
    def __init__(self):
        self.lst = [12, 3, 4]

    def __str__(self):
        return str(self.lst)
    
    def __getitem__(self, i):
        return self.lst[i]

ob = Test()

print(ob)
print(ob.lst)
print(f'value in index \'1\' is = {ob[1]}')

print('-------------------------------------')

class Test:
    def __init__(self):
        self.lst = [12, 3, 4]

    def __str__(self):
        return str(self.lst)
    
    def __getitem__(self, i):
        return self.lst[i]
    
    def __setitem__(self, i, v):
        self.lst[i] = v

ob = Test()
print(ob)
ob[1] = 22
print(ob)
print(f'value in index \'1\' after change = {ob[1]}')

print('-------------------------------------')

class Clock:
    def __init__(self, h, m, s):
        self.h = h 
        self.m = m
        self.s = s
    
    def __str__(self):
        return str(str(self.h) + ':' + str(self.m) + ':' + str(self.s))
    
ob = Clock(4,15,36)
print(ob)

print('-------------------------------------')

class Address:
    def __init__(self, city, street, zipcode):
        self.city = city 
        self.street = street 
        self.zipcode = zipcode
    
    def __str__(self):
        return f'{self.city}--{self.street}--{self.zipcode}'

ob = Address('Neyshabour', 'Khatam', '421')        
print(ob)


print('-------------------------------------')

class Robot:
    def __init__(self, name, year):
        self.name = name 
        self.year = year

    def __str__(self):
        return 'naem : ' + self.name + ', build-year : ' + str(self.year)
    
    def __repr__(self):
        return 'robot(\"' + self.name + '\" , ' + str(self.year) + ')'  
    
ob = Robot('sepehr', '2003')
print(ob)
print(repr(ob))

print('-------------------------------------')

class C:
    def __init__(self, size, x, y):
        self.size = size
        self.x = x
        self.y = y

    def __call__(self, x, y):
        self.x = x
        self.y = y

ob = C(500, 100, 50)
print(ob.size)
print(ob.x)
print(ob.y, end='\n\n')

ob(20, 70)
print(ob.size)
print(ob.x)
print(ob.y)

print('-------------------------------------')

class Complex:
    def __init__(self, a, b):
        self.a = a
        self.b = b
    
    def __add__(self, o):
        x = self.a + o.a
        y = self.b + o.b
        return str(x) + ' + ' + str(y) + 'j'

ob1 = Complex(3, 7)
ob2 = Complex(2, 3)
ob3 = ob1 + ob2
print(ob3)

print('-------------------------------------')

class Test:
    def __init__(self, a):
        self.a = a 

    def __add__(self, o):
        return self.a + o.a

ob1 = Test(3)
ob2 = Test(2)
ob3 = ob1 + ob2
print(ob3)

ob1 = Test("ali")
ob2 = Test("reza")
ob3 = ob1 + ob2
print(ob3)

print('-------------------------------------')

class Test:
    def __init__(self, a):
        self.a = a

    def __gt__(self, o):
        if self.a > o.a:
            return True
        else:
            return False
        
    def __lt__(self, o):
        if self.a < o.a:
            return True
        else:
            return False

    def __eq__(self, o):
        if self.a == o.a:
            return True
        else:
            return False

ob1 = Test(3)
ob2 = Test(6)

print(ob1 > ob2)
print(ob1 < ob2)
print(ob1 == ob2)

print('-------------------------------------')

class A:
    def __init__(self, a):
        print('init')
        self.__set__(self, a)
    
    def __set__(self, i, v):
        print('set')
        print(i)
        self.v = v
        print(self.v)

    def __get__(self, i, o):
        print(o)
        print('get')
        return self.v + 1
        
class B:
    x = A(5)

ob = B()
ob.x = 8
print(ob.x)