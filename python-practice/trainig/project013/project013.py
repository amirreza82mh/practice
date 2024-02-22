def f(n: int | float) -> int | float:
    '''
    double
    '''
    return n * 2

print(f(3))

#lamda
g = lambda n : n * 2
print(g(3))

print('\n######################\n')

add = lambda number1, number2 : number1 + number2
print(add(3, 4))

print('\n######################\n')

add = lambda number1, number2 : (number1 + number2, number1-number2)
print(add(3, 4))

print('\n######################\n')

hi = lambda : print('hello')
hi()

print('\n######################\n') 

d = {'a' : 3, 'b' : 7, 'c' : 5}
print(d[max(d.keys() , key = lambda k : d[k])])

print('\n######################\n') 

#map
lst = ['ali', 'reza']
u = list()
for i in lst:
    u.append(i.upper())
print(u)

#or
m = map(str.upper,  lst)
print(list(m))

print('\n######################\n')

name  = ['ali', 'reza']
grade = [13, 18]

x = zip(name, grade)
print(list(x))

print(list(map(lambda x, y : (x, y), name, grade)))

print('\n######################\n')

lst = ['a' , 'b']
x = []
for i in lst:
    x.append(ord(i))
print(x)

print(list(map(ord, lst)))

print('\n######################\n')

scores = [12, 8, 19, 15, 7]
print(list(map(lambda x : x > 10, scores)))

#filter
scores = [12, 8, 19, 15, 7]
print(list(filter(lambda x : x > 10, scores)))

print('\n######################\n')

lst1 = [3, 2, 1]
lst2 = [6, 4, 7]

#add index of arrays
print(list(map(lambda x , y : x + y,  lst1, lst2)))

print('\n######################\n')

#with using function 
def sum_function(number1: int , number2: int) -> int:
    return number1 + number2

lst1 = [3, 2, 1]
lst2 = [6, 4, 7]
print(list(map(sum_function,  lst1, lst2)))

print('\n######################\n')

def f(x):
    return x + 5

def g(y):
    return y * 2

func = [f, g]

lst = [1, 2 ,3]

for i in lst:
    print(list(map(lambda fun: fun(i), func)))

print('\n######################\n')

lst = ['radar', 'ali', 'madam', 'php']
palindrom = lambda x : (x == ''.join(list(reversed(x)))) #hint: reversed return list
print(list(filter(palindrom, lst)))

print('\n######################\n')

lst = [2, 7, '', 9, {}, 8, [], 12]
print(list(filter(None, lst)))

print('\n######################\n')

from functools import reduce

lst = [4, 8, 3, 5]
print(reduce(lambda a, b : a + b, lst))

def func(x, y):
    return x + y

print(reduce(func, lst))

#write reduce my self
def my_reduce(func, sequance):
    r = sequance[0]
    for i in sequance[1:]:
        r = func(r, i)
    return r

print(my_reduce(func, lst))

print('\n######################\n')

lst = [5, 2, 3, 1, 4]
sort = sorted(lst)
print(sort)

#or
sort = lambda x : sorted(x)
print(sort(lst))

#or
lst.sort()
print(lst)

print('\n######################\n')

student=[
    {'id' : 1, 'name' : 'taha', 'score' : 19},
    {'id' : 6, 'name' : 'sara', 'score' : 8},
    {'id' : 4, 'name' : 'omid', 'score' : 15},
    {'id' : 3, 'name' : 'mahsa', 'score' : 19}
]

f = lambda lst : lst['score']
print(sorted(student, key = f))

'''[
    {'id': 6, 'name': 'sara', 'score': 8},
    {'id': 4, 'name': 'omid', 'score': 15},
    {'id': 1, 'name': 'taha', 'score': 19},
    {'id': 3, 'name': 'mahsa', 'score': 19}
]
'''

print('\n######################\n')

student=[
    (1, 'taha',   19),
    (6, 'sara',   8),
    (4, 'omid',   15),
    (3, 'mahsa',  19)
]

from operator import itemgetter

print(sorted(student, key = itemgetter(2)))

'''
[(6, 'sara', 8),
(4, 'omid', 15),
(1, 'taha', 19),
(3, 'mahsa', 19)]
'''

print('\n######################\n')

student=[
    (1, 'taha',   19),
    (6, 'sara',   8),
    (4, 'omid',   15),
    (3, 'mahsa',  19)
]

from operator import itemgetter

print(sorted(student, key = itemgetter(2), reverse = True))

'''
[
    (1, 'taha', 19),
    (3, 'mahsa', 19),
    (4, 'omid', 15),
    (6, 'sara', 8)
    ]
'''

print('\n######################\n')

student=[
    (1, 'taha',   19),
    (6, 'sara',   8),
    (4, 'omid',   15),
    (3, 'mahsa',  19)
]

from operator import itemgetter

print(sorted(student, key = itemgetter(2, 1)))

'''
[
    (6, 'sara', 8),
    (4, 'omid', 15),
    (3, 'mahsa', 19),
    (1, 'taha', 19)
    ]
'''

print('\n######################\n')

d = {'a' : 3, 'b' : 7, 'c' : 5}
print(sorted(d.items() , key = lambda x : x[1]))