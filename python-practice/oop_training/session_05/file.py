#inheritance

from typing import Any


class Person:
    def __init__(self, name):
        self.name = name
    
    def show(self):
        print('name:', self.name)

class Student(Person):
    def __init__(self, name, score):
        # Person.__init__(self, name)
        super().__init__(name)
        self.score = score

    def call(self):
        print('welcome', self.name)

stu = Student('amirreza', 20)
stu.call()
stu.show()

del Person

print("\n===================================\n")

class Person:
    def __init__(self, name, identy):
        self.name = name 
        self.identy = identy
    
    def show_info(self):
        print(self.name + " : " + str(self.identy))

class Employee(Person):
    def __init__(self, name, identy, salary, post):
        super().__init__(name, identy)
        self.salary = salary
        self.post = post

    def show_all(self):
        print(f"hello my name is {self.name}, with id number : {self.identy}, my salary in post {self.post} is {self.salary}")        
    

emp = Employee('amirreza', '40018263', '500000', 'modir')
emp.show_info()
emp.show_all()

print("\n===================================\n")

class Rectangle:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def area(self):
        return self.x + self.y

class Square(Rectangle):
    def __init__(self, z):
        super().__init__(x=z, y=z)

r = Rectangle(2, 3)
print(r.area())    

s = Square(5)
print(s.area())

print()
#__mro__ = Method resolution order
print(Square.__mro__)
print(Rectangle.__mro__)

print("\n===================================\n")

#multiple inheritiance

class B1:
    def __init__(self, x):
        self.x = x
        print(self.x)

class B2:
    def __init__(self, y):
        self.y = y
        print(self.y)

class D(B1, B2):
    def __init__(self, z):
        self.z = z
        print(self.z)
        B1.__init__(self, 2)
        B2.__init__(self, 3)

ob = D(1)

print("\n===================================\n")

class Square:
    def __init__(self, x):
        self.x = x

    def perimeter(self):
        return self.x * 4
    
    def S_area(self):
        return self.x * self.x

class Triangle:
    def __init__(self, x, h):
        self.x = x
        self.h = h

    def T_area(self):
        return self.x * self.h / 0.5

class Pyramid(Square, Triangle):
    def __init__(self, x, h):
        self.x = x 
        self.h = h
        Square.__init__(self, x=x)
        Triangle.__init__(self, x=x, h=h)
    
    def P_area(self):
        return Square.S_area(self) + 0.5 * Square.perimeter(self) * self.h
    
    def __str__(self):
        return str(Square.S_area(self) + 0.5 * Square.perimeter(self) * self.h)

ob = Pyramid(2, 5)
print(ob.P_area())
print()
print(ob)

print("\n===================================\n")

#multilevel inheritance

class A:
    def __init__(self, name):
        self.name = name

    def getname(self):
        return self.name
    
class B(A):
    def __init__(self, name, age):
        self.age = age
        super().__init__(name)
    
    def getage(self):
        return self.age

class C(B):
    def __init__(self, name, age, score):
        self.score = score
        super().__init__(name, age)
    
    def getscore(self):
        return self.score

ob = C('Amir', 20, 19)
print(ob.getname())
print(ob.getage())
print(ob.getscore())

print("\n===================================\n")

class Employee:
    def __init__(self, name, identy):
        self.name = name
        self.identy = identy

class HE(Employee):
    def __init__(self, name, identy, hw, hr):
        self.hw = hw
        self.hr = hr
        super().__init__(name, identy)

    def salary(self):
        return self.hw * self.hr


class ME(Employee):
    def __init__(self, name, identy, mr):
        self.mr = mr
        super().__init__(name, identy)

    def salary(self):
        return self.mr


class CE(ME):
    def __init__(self, name, identy, mr, cr):
        self.cr = cr
        super().__init__(name, identy, mr)

    def salary(self):
        return super().salary() + self.cr

class P():
    def salary(self, a):
        for i in a:
            print(f"{i.identy}: \"{i.name}\" with salary:{i.salary()}")

ob1 = HE('sara', 1, 4, 100000)
ob2 = ME('ali', 2, 3000000)
ob3 = CE('amir', 3, 3000000, 500000)       

ob = P()
ob.salary([ob1,ob2,ob3])

print("\n===================================\n")

#diamond problem

class A:
    def h(self):
        print('A')

class B(A):
    def h(self):
        print('B')

class C(A):
    def h(self):
        print('C')

class D(B, C):
    pass

ob = D()
ob.h()

print('------------')


class A:
    def h(self):
        print('A')

class B(A):
    def h(self):
        print('B')

class C(A):
    def h(self):
        print('C')

class D(C, B):
    pass

ob = D()
ob.h()

print("\n===================================\n")

class A:
    def __init__(self, x, y):
        self._x = x         #protected
        self.__y = y        #private
    
    def h(self):
        print(self._x)
        print(self.__y)

class B(A):
    def __init__(self, x, y):
        super().__init__(x, y)

    def g(self):
        print(self._x)
        # print(self.__y)        Error

ob = B(1, 2)
ob.h()
print()
ob.g()

print("\n===================================\n")

class A:
    def __f(self):
        return 'A'

    def g(self):
        print(self.__f())

class B(A):
    def __f(self):
        return 'B'
    
ob = B()
ob.g()

print('------------')

class A:
    def _f(self):
        return 'A'

    def g(self):
        print(self._f())

class B(A):
    def _f(self):
        return 'B'
    
ob = B()
ob.g()