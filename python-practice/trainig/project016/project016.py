import re

txt = 'python is a programming language.'

print('--------------')

m = re.search('python', txt)
print(m)

print('--------------')

m = re.search('amir', txt)
print(m)

print('--------------')

m = re.search('^python', txt)
if m: 
    print('Yes')
else:
    print('No')

print('--------------')

m = re.search('^pyth', txt)
n = re.search('^pythog', txt)
print(m)
print(n)

print('--------------')

m = re.search('language.$', txt)
if m: 
    print('Yes')
else:
    print('No')

print('--------------')

m = re.search('programming$', txt)
if m: 
    print('Yes')
else:
    print('No')

print('\n#################\n')

txt = 'phone number 091212123344 and other 02122334455 number'

m = re.search('number \d+', txt)
print(m)
print(m.group(0))
# print(m.group(1))  ERROR

print('--------------')

m = re.search('number (\d+)', txt)
print(m)
print(m.group(0))
print(m.group(1))

print('--------------')

m = re.search('(\w+) (\d+)', txt)
print(m)
print(m.group(0))
print(m.group(1))
print(m.group(2))

print('--------------')

print(re.findall('\d+', txt))
print('--------------')
print(re.findall('\d+ \w+', txt))
print('--------------')
print(re.findall('\w+ \d+', txt))
print('--------------')
print(re.findall('[0-9]+', txt))
print('--------------')
print(re.findall('[0-2]+', txt))
print('--------------')
print(re.findall('[0-9]', txt))

print('\n#################\n')

txt = 'Amir Reza  Mehrabani'

print(re.findall('r', txt))
print(re.findall('m', txt))
print(re.findall('[m-r]', txt))
print(re.findall('\s+', txt))
print(re.findall('\S+', txt))
print(re.findall('r[^ ]', txt))
print(re.findall('r[^ ]+', txt))
print(re.findall('r[^ ]*', txt))
print(re.findall('r[^a]*', txt))

print('\n#################\n')

txt = 'from amirreza82mh@gmail.com to ali@gmail.com'

m = re.findall('\w+@\w+.\w+', txt)
print(m)

#or
m = re.findall('\S+@\S+', txt)
print(m)

print('--------------')

print(re.split('\s', txt))
print(re.split('\s', txt, 1))

print('\n#################\n')

txt = 'python is a programming language.'

print(re.sub('\s', '_', txt))
print(re.sub('\s', '_', txt, 2))
print(re.sub('\S', '_', txt))
print(re.sub('\S+','_',txt))

print('\n--------------\n')

txt = '0902-464-9494'

print(re.sub('-', '#', txt))
print(re.sub('\D', '#', txt))
print(re.sub('\d', '#', txt))
print(re.sub('\d+', '#', txt))

print('--------------')

txt = '  Amir Reza   '

print(re.sub('^\s+', '', txt))
print(re.sub('\s+$', '', txt))
print(re.sub('^\s+$', '', txt))
print(re.sub('\s', '', txt))

print('\n#################\n')

txt = 'ABCDEFCGH'

print(re.subn('CD', 'X', txt))
print(re.subn('C', 'X', txt))

print('\n--------------\n')

txt = 'ABCDEFCGH'

r = re.search('CDE', txt)
print(r)

s = r.start()
e = r.end()
print(s, e)

txt = txt[ : s] + txt[e : ]
print(txt)

print('\n#################\n')

txt = 'He was carefully disguised but captured quickly by police.'

print(f'text = {txt}')
print(re.findall('\w+ly', txt))

fi = re.finditer('\w+ly', txt)
for i in fi:
    print(i.start(), i.end(), i.group(0))

