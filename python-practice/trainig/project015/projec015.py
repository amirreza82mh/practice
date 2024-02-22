# try:
#     f = open('test.txt','r')
# except FileNotFoundError as fe:
#     print(fe)

# print('hi')

f = open('myfile.txt', 'w')
line1 = 'hello world\n'
line2 = 'i love python\n'
line3 = str(52)
f.write(line1)
f.write(line2)
f.write(line3)
print(f.name)
print(f.mode)
f.close()

print('-------------')

with open('myfile2.txt', 'w') as f:
    line1 = 'hello world\n'
    line2 = 'i love python\n'
    line3 = str(52)
    f.write(line1)
    f.write(line2)
    f.write(line3)

with open('myfile.txt', 'r') as myfile:
    print(myfile.readline())
    print(myfile.readline())

print('-------------')

with open('myfile.txt', 'r') as myfile:
    print(myfile.readlines())

print('-------------')

with open('myfile.txt', 'r') as myfile:
    print(myfile.read(3))
    print(myfile.read(10))

print('-------------')

with open('myfile.txt', 'r') as myfile:
    for line in myfile:
        print(line, end = '')

print('\n-------------')

with open('myfile.txt', 'r') as myfile:
    print(myfile.read())

print('-------------')

#remove file
import os
n = 'myfile2.txt'
print(os.path.exists(n))
os.remove(n)

print('-------------')

name1 = 'myfile.txt'
name2 = 'copy.txt'

with open(name1, 'r') as f:
    with open(name2, 'w') as cop:
        n = f.read()
        cop.write(n)

with open(name2, 'r') as cop:
    for line in cop:
        print(line, end = '')

print('\n-------------')

name1 = 'myfile.txt'
name2 = 'copy.txt'

with  open(name1, 'r') as f , open(name2, 'w') as cop:
    for line in f:
        cop.write(line)

with open(name2, 'r') as cop:
    print(cop.read())

print('-------------')

if os.path.exists('copy.txt'):
    os.remove('copy.txt')

if os.path.exists('myfile.txt'):
    os.remove('myfile.txt')

print('-------------')

name1 = 'first.txt'
name2 = 'second.txt'
name3 = 'thied.txt'

with open(name1, 'w') as f1:
    f1.write('ali\n')
    f1.write('sara\n')

with open(name2, 'w') as f2:
    f2.write('taha\n')
    f2.write('omid\n')
    f2.write('mahsa')

with open(name1, 'r') as f1, open(name2, 'r') as f2:
    data1 = f1.read()
    data2 = f2.read()

with open(name3, 'w') as f3:
    f3.write(data1 + data2)

os.remove(name1)
os.remove(name2)
os.remove(name3 )

print('-------------')

lst = ['yes', 'no', 'no', 'yes', 'yes', 'yes', 'no']

name = 'file.txt'

with open(name, 'w') as f:
    for i in lst:
        f.write(i + '\n')

yes = 0
no = 0
string = ''

with open(name, 'r') as f:
    for line in f:
        string += line

        if string.strip() == 'yes':
            yes += 1
            string = ''
        elif string.strip('\n') == 'no':
            no += 1
            string = ''

print(f'the number of yes = {yes}')
print(f'the number of no = {no}')
    
print('-------------')

lst = ['yes', 'no', 'no', 'yes', 'yes', 'yes', 'no']

name = 'file.txt'

with open(name, 'w') as f:
    for i in lst:
        f.write(i + '\n')

yes = 0
no = 0

with open(name, 'r') as f:
    lst = f.readlines()
    for i in lst: 
        x = i.strip()
        if x == 'yes':
            yes += 1
        else:
            no += 1

print(f'the number of yes = {yes}')
print(f'the number of no = {no}')

print('-------------')

lst = ['yes', 'no', 'no', 'yes', 'yes', 'yes', 'no']

name = 'file.txt'

with open(name, 'w') as f:
    for i in lst:
        f.write(i + '\n')

d = dict()

with open(name, 'r') as f:
    for line in f:
        w = line.split()
        for i in w:
            d[i] = d.get(i, 0) + 1

print(d)

print('-------------')

def count(filename: str) -> int:
    c = 0
    with open(filename, 'r') as f:
        for line in f:
            c += 1
    return c  

print(f'number of lines: {count(name)}')

print('-------------')

def count(filename: str):
    try:
        with open(filename, 'r') as f:
            x = f.read()
    except:
        print('file dose not exist')
    else:
        v = x.splitlines()
        c = len(v)
        print(c)

lst = [name, 'asdfas.txt']

list(map(count, lst))

os.remove(name)

print('-------------')

filename ='test.txt'

with open(filename, 'w') as f:
    f.write('ABCDEFG')

with open(filename, 'r') as f:
    print(f.read(1))
    print(f.tell())
    print(f.read(2))
    print(f.tell())
    f.seek(0, 0)
    print(f.read(2))
    print(f.tell())
    f.seek(1, 0)
    print(f.tell())

print('-------------')

with open(filename, 'rb') as f:
    print(f.read(1))
    print(f.tell())
    print(f.read(2))
    print(f.tell())
    f.seek(0, 0)
    print(f.read(2))
    print(f.tell())
    f.seek(1, 0)
    print(f.tell())
    f.seek(-5, 2)
    print(f.read(1))

os.remove(filename)

print('-------------')

line1 = 'ali\n'
line2 = 'sara'

lst = [line1, line2]

with open('file.txt', 'w') as f:
    f.writelines(lst)

with open('file.txt', 'r') as f:
    print(f.read())

print('-------------')

line3 = '\nmahsa'
with open('file.txt', 'a') as f:
    f.write(line3)

with open('file.txt', 'r') as f:
    print(f.read())

os.remove('file.txt')

print('-------------')

#binay

x = b'AmiReza'
print(x)
print(x.decode())

print()

b = bytes([65, 97])
print(b)
print(b.decode())

print()

a = bytearray([65, 97])
print(a)
print(a.decode())

print('-------------')

data = 'hello\npython'
print(data)
print(type(data))

print()

b = bytes(data, 'utf-8')
print(b)
print(b.decode())
print(type(b))

print()

with open('file.bin', 'wb') as f:
    print(f.write(b))

os.remove('file.bin')

print('-------------')

import json

d = {'k1' : 'v1', 'k2' : 'v2'}

js = json.dumps(d)
print(js)

print()

js = json.dumps(d, indent = 4, separators = (';', '='))
print(js)

with open('j.json', 'w') as f:
    json.dump(d, f)

with open('j.json', 'r') as f:
    print(json.load(f))

print('-------------')
print('-------------')

import pickle

with open('p.bin', 'wb') as f:
    pickle.dump(d, f)

with open('p.bin', 'rb') as f:
    print(pickle.load(f))

print('-------------')

import csv
x = ['Name', 'Age']
r1 = ['ali', 35]
r2 = ['taha', 10]
r3 = ['mahsa', 40]

with open('d.csv', 'w') as f:
    w = csv.writer(f)
    w.writerow(x)
    w.writerows([r1, r2, r3])

with open('d.csv', 'r') as f:
    r = csv.reader(f)
    for i in r:
        print('   '.join(i))

print('-------------')

import glob
print(glob.glob('~/amir'))

import pandas as pd
data = pd.read_csv('d.csv')
print(data)

data.to_csv('f.csv', sep = ';', index = False)