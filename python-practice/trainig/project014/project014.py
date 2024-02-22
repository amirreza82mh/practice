'''
#TypeError

s = 'ali'
print(s + 2)
'''

'''
#NameError

print(a)
'''

'''
#AtrributeError

s = 'ali'
s.append('reza)
'''

'''
#IndexError

lst = [15, 20, 17]
print(lst[3])
'''

'''
#keyError

d = {'a' : 5}
print(d{'f'})
'''

# x = 8 / 0  ZeroDivisionError

print('\n################\n')

try:
    print(k)
except NameError:
    print('Error')

print('hello')

print('\n################\n')

try:
    print(k)
except NameError as ne:
    print(ne)

print('\n################\n')

s = 'ali'

try:
    print(s + 2)
except TypeError as te:
    print(te)

print()

try:
    print(s + 2)
except TypeError:
    print('Error')

print('\n################\n')

try:
    x = 8 / 0
except ZeroDivisionError as ze:
    print(ze)

print()

try:
    x = 8 / 2
except ZeroDivisionError as ze:
    print(ze)
else:
    print(x)

print('\n################\n')

def divide(x, y):
    try:
        r = x / y
    except ZeroDivisionError as ze:
        print(ze)
    else:
        print(r)
    finally:
        print('ha ha ha')

divide(4, 2)
print()
divide(4, 0)

print('\n################\n')

s = 'a'

try:
    i = int(s)
except ValueError:
    i = -1
finally:
    print(i)

print('\n################\n')

def f(n : int):
    try:
        if n == 13:
            raise ValueError('unlucky number')
        else:
            return 20 / n
    except (ZeroDivisionError, TypeError) as e:
        return e

print(f(5))
print()
print(f(0))
print()
print(f('a'))
print()
# print(f(13))   

print('\n################\n')

try:
    print(20 / 0)
    try:
        print(n)
    except NameError as ne:
        print(ne)
except ZeroDivisionError as ze:
    print(ze)

print('\n################\n')

try:
    print(20 / 5)
    try:
        print(n)
    except NameError as ne:
        print(ne)
except ZeroDivisionError as ze:
    print(ze)

print('\n################\n')

try:
    n = int(input('Enter an even number: '))
    assert n % 2 == 0
except:
    print('the number is not even !?')
else:
    print(n * 2)