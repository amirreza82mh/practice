###
###function
###

def hello():
    print('Hello world #1')

hello()
print('ali')
hello()

print('----------------')

def hello_2():
    return 'Hello world #2'

s = hello()
print(s)

print('----------------')

def hello_3(p):
    print(p)

s = 'Hello world #3'
hello_3(s)

print('----------------')

def addtwo(a, b):
    return a + b

c = addtwo(2, 3)
print(c)

print('----------------')

def f(a):
    a *= 2
    print(a)
    return a+1

b = 10
r = f(b)
print(r)

print('----------------')

def f(x, y):
    if x > y:
        return x
    else:
        return y

c = f(10 , 54)
print(c)

print('----------------')

def h(x, y, z):
    max = x
    if y > max:
        max = y
    elif z > max:
        max = z
    return max

r = h(23 , 5 , 25)
print(r)

print('----------------')

def g(x, y, z):
    return(x, f(y, z))

r = g(23 , 5 , 25)
print(r)

print('----------------')

PI = 3.14

def Area(r):
    return PI * r * r

def Perimeter(r):
    return PI * r * 2

def main():
    r = 4
    print(Area(r))
    print(Perimeter(r))

main()

print('----------------')

x = 1

def f():
    x = 2
    print(x)

f()
print(x)

print('----------------')

x = 1

def f():
    global x
    x = 2
    print(x)

f()
print(x)

print('----------------')

x = 5

def f():
    global x
    print(x)
    x = 8 
    print(x)

f()
print(x)

print('----------------')

def f(a, b):
    a += 1
    b -= 1
    return a, b

x = 5 
y = 12
m, n = f(x, y)
print(m ,n)

print('----------------')

def f(x, y, z):
    min = x
    max = x

    if y > max:
        max = y
    if y < min:
        min = y
    if z > max:
        max = z
    if z < min:
        min = z
    return max, min

max, min = f(5, 7, 9)
print(max)
print(min)

print('----------------')

def f(a):
    a[0] += 1
    a[1] -= 1

lst = [5 , 12]
f(lst)
print(lst)

print('----------------')

def f(a):
    a['a'] += 1
    a['b'] -= 1

my_dict = {'a' : 5 , 'b' : 12}
f(my_dict)
print(my_dict)

print('----------------')

def f(a, b):
    print(a ,b)

f(1, 2)
f(a = 1, b = 2)
f(1 , b = 2)
f(b = 1 , a = 2)
# f(a = 1, 2)
# f(1 , a = 2)

print('----------------')

def f(a, b=5, c=7):
    print(a,b,c)

f(1)
f(1, 3)
f(1, 3, 5)
f(1 , c=9)
f(b=3, a=1, c=5)
# f(1, b=2, 3)

print('----------------')
#keyword only argument

def f(*, a=3):
    print(a)

f()
f(a=5)
# f(5)    #f() takes 0 positional arguments but 1 was given

print('----------------')
#var argument

def f(*t):
    s = 0
    for i in t:
        s += i
    print(s)

f(1, 2, 3)
f(4, 5)

print('----------------')

def add(a, b, *more):
    r = a + b + sum(more)
    print(r)

add(1, 2, 3)
add(4, 5)
add(1, 4, 7, 9, 13, 23)

print('----------------')

def f(a, b, *more):
    print(more)

f(1, 2, 3, 4, 5)

print('----------------')

def f(*t, x=5):
    print(t)
    print(f'number = {x}')

f(1, 2, 3)
f(1, 2, x=3)
#f(1, x=3, 2)

print('----------------')

def concat(*s, sep='.'):
    return sep.join(s)

print(concat('ali', 'reza'))
print(concat('amir', 'reza', 'mehrabani'))
print(concat('amir', 'reza', sep='/'))

print('----------------')

def concat(*s, f='unknow', sep='.'):
    l = ['']
    l[0] = sep.join(s)
    sep = '/'
    l.append(f)
    print(sep.join(l))

concat('amir', 'reza', f='mehrabani')

print('----------------')

def f(a, *, b=2, c=3):
    print(a , b , c)

f(1)
f(2, b=3)
# f(1, 2, c=5)
# f(1, b=4, 6)

print('----------------')

def f(a, b, **c):
    print(a, b, c)

f(3, 4, x=5, y=9)

print('----------------')

# def f(a, b, **c, *d):
#     print(a, b, c, d)

# f(1, 3, x=5, y=7, 9, 11, 13)

print('----------------')

def f(a, b, *c, **d):
    print(a)
    print(b)
    print(c)
    print(d)

f(1, 3, 9, 11, 13, x=5, y=7)

print('----------------')

count_dict = {'L' : 0, 'U' : 0}

def func_count(s):
    for ch in s:
        if ch.islower():
            count_dict['L'] += 1
        else:
            count_dict['U'] += 1

s = "AMIRreza"
func_count(s)
print(count_dict)

print('----------------')

def count_char(s):
    d = {}
    for ch in s:
        if ch in d:
            d[ch] += 1
        else:
            d[ch] = 1
    return d

print(count_char('agham ali reza'))

print('----------------')

def word_count(s):
    d = {} 
    l = s.split(' ')
    for i in l:
        if i in d:
            d[i] += 1
        else:
            d[i] = 1
    return d

s = 'python created by rossum python'
print(word_count(s))

print('----------------')

def switch(a):
    d = {1 : 'one' , 2 : 'two'}
    return d.get(a , 'nothing')

print(switch(1))
print(switch(2))
print(switch(6))

print('----------------')

def switch(a):
    d = {1 : 'sunday',
         2 : 'monday',
         3 : 'tuesday',
         4 : 'wednesday',
         5 : 'thurseday',
         6 : 'friday',
         7 : 'saturday'}
    return d.get(a, 'nothing')

print(switch(1))
print(switch(3))
print(switch(8))

print('----------------')

grade_student = [
    {'id' : 1 , 'M' : 40 , 'F' : 60},
    {'id' : 2 , 'M' : 80 , 'F' : 70}
]

def ave_grade(lst):
    for i in lst:
        x = i.pop('M')
        y = i.pop('F')
        
        i['Ave'] = (x + y) / 2

    return lst

print(ave_grade(grade_student))