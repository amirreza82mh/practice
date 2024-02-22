class Test:
    """
    class for add and mul
    """
    def set_var(self, a, b):
        self.a = a
        self.b = b
    
    def add(self):
        return self.a + self.b
    
    def mul(self):
        return self.a * self.b
    
ob1 = Test()
ob1.set_var(3, 4)
print(ob1.__dict__)
print(ob1.__doc__)
print("a in ob1 = " + str(ob1.a))
print("b in ob1 = " + str(ob1.b))
print("sum ob1 = " + str(ob1.add()))
print("mul ob1 = " + str(ob1.mul()))

print("------------------------------------------")

ob2 = Test()
ob2.set_var(7, 8)
print(ob2.__dict__)
print(ob2.__doc__)
print("a in ob2 = " + str(ob2.a))
print("b in ob2 = " + str(ob2.b))
print("sum ob2 = " + str(ob2.add()))
print("mul ob2 = " + str(ob2.mul()))
del ob2

# print(ob2.a)   ERROR

print("------------------------------------------")

class Test:
    def __init__(self, a, b):
        self.a = a
        self.b = b
    
    def add(self):
        return self.a + self.b
    
    def mul(self):
        return self.a * self.b

ob1 = Test(3, 4)
print("a in ob1 = " + str(ob1.a))
print("b in ob1 = " + str(ob1.b))
print("sum ob1 = " + str(ob1.add()))
print("mul ob1 = " + str(ob1.mul()))

print("------------------------------------------")

class Book:
    def __init__(self, author, title):
        self.author = author
        self.title = title

    def info(self):
        print(self.title + ": " + self.author)


ob1 = Book('Amirreza' , 'pyhton')
ob1.info()

print("------------------------------------------")

class Student:
    def __init__(self, name, grade):
        self.d = dict()
        self.d['name'] = name
        self.d['grade'] = grade
    
    def get_stu(self):
        return self.d

lst = list()
mahsa = Student('mahsa', 20)
ali = Student('ali', 18)
lst.append(mahsa.get_stu())
lst.append(ali.get_stu())
print(lst)
print(lst[0])
print(lst[1])

print("------------------------------------------")

import math

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def primeter(self):
        return 2 * self.radius * math.pi 

    def area(self):
        return self.radius * self.radius * math.pi

shape1 = Circle(5)
print(shape1.__dict__)
print("perimeter of shape1 = " + str(shape1.primeter()))
print("area of shape1 = " + str(shape1.area()))

print(isinstance(shape1, Circle))
print(isinstance(ob1, Circle))

print("------------------------------------------")

a = 3
print(type(a))   #<class 'int'>
print(isinstance(a, int))

print()

d = dict()
print(type(d))   #<class 'dict'>
print(isinstance(d, dict))
print(isinstance(d, int))

print("------------------------------------------")

class counter:
    def __init__(self, number):
        self.number = number
    
    def up(self):
        self.number += 1
    
    def down(self):
        self.number -= 1

number1 = counter(7)
number1.down()
number1.down()
print(number1.__dict__)
number1.up()
print(number1.__dict__)

print("------------------------------------------")

class C:
    def __init__(self):
        self.s = ''

    def get_string(self):
        self.s = input("Enter a string: ")

    def show(self):
        print(self.s.upper())

ob = C()
# ob.get_string()
ob.show()

class Complex:
    def __init__(self, a, j):
        self.a = a
        self.j = j
    
    def show(self):
        print(str(self.a) + ' + ' + str(self.j) +'j')

num1 = Complex(4, 5)
num1.show()

print("------------------------------------------")

class Email:
    def t(self):
        self.sent = True
    
    def f(self):
        self.sent = False

ob = Email()
ob.t()
print(ob.sent)

ob.f()
print(ob.sent)

print("------------------------------------------")

class Machine:
    model = 'peugeot'

    def __init__(self, t):
        self.t = t

ob1 = Machine('206')
ob2 = Machine('207')

print(ob1.model)
print(ob2.model)

print(ob1.t)
print(ob2.t)

print("------------------------------------------")

class C:
    lst = list()

    def __init__(self, name):
        self.name = name
    
    def f(self, x):
        self.lst.append(x)

ob1 = C('A')
ob2 = C('B')

ob1.f(1)
ob1.f(2)
ob1.f(3)

print(ob1.lst)
print(ob2.lst)

ob2.f(4)

print(ob1.lst)
print(ob2.lst)

print("------------------------------------------")

class C:

    def __init__(self, name):
        self.name = name
        self.lst = list()
    
    def f(self, x):
        self.lst.append(x)

ob1 = C('A')
ob2 = C('B')

ob1.f(1)
ob1.f(2)
ob1.f(3)

print(ob1.lst)
print(ob2.lst)

ob2.f(4)

print(ob1.lst)
print(ob2.lst)

print("------------------------------------------")

class Student:
    stream = 'cse'      # class variable

    def __init__(self, name, score):
        self.name = name    # instance variable
        self.score = score  # instance variable

st1 = Student('Amir', 19.20)
st2 = Student('hedayat', 19.00)

print(st1.name)
print(st2.name)

print(st1.stream)
print(st2.stream)

print('class variable = ' + Student.stream)

print("------------------------------------------")

class Test:
    def __init__(self, a, b):
        self.a = a
        self.__b = b

    def f(self):
        self.__b += 2
        print(self.__b)

ob1 = Test(3, 5)
print(ob1.a)
ob1.a = 1
print(ob1.a)
#print(ob1.__b)

print(ob1.__dict__)

print(ob1._Test__b)  #name mangling
print("------------------------------------------")

class Test:
    def __init__(self, a):
        self.__a = a

    def f(self):
        print(self.__a , end = " ")
        self.__a += 1
        return(self.__a)
    
    def g(self, m):
        print(m + self.f())

ob = Test(5)

print(ob.f())
ob.g(5)

print("------------------------------------------")

class Test:
    __x = 15

    def f(self):
        return self.__x + 1

ob = Test()
print(ob.__dict__)
print(ob.f())

print("------------------------------------------")

class Test:
    def __init__(self, a):
        self.a = a
    
    def __f(self):
        return(self.a)
    
    def g(self):
        print(self.__f())

ob = Test(5)

ob.g()

print(ob._Test__f(), end='')