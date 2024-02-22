def reverse_string(s):
    a = s[ : : -1]
    return a

string = 'amirreza mehrabani'
rev_string = reverse_string(string)
print(rev_string)
string = 'abc'
rev_string = reverse_string(string)
print(rev_string)

print('\n############################\n')

def palindrome(s):
    a = s[ : : -1]
    return a == s

string = 'radar'
print(string)
print(palindrome(string))

print('\n############################\n')

def slice_string(s, start, end):
    a = s[0 : start] + s[end+1 : ]
    return a

string = 'pythorn'
print(string)
print(slice_string(string, 1, 3))

print('\n############################\n')

def remove_indexeven(s):
    a = ''
    for i in s:
        if s.index(i) % 2 == 0:
            a = a + s[s.index(i)]
    return a

string = 'amirreza mehrabani'
print(string)
print(string.index('m'))
print(remove_indexeven(string))

print('\n############################\n')

def unique_list(lst):
    b = []
    for i in lst:
        if i not in b:
            b.append(i)
    return b

a = [1, 2, 3, 1, 4, 2]
print(a)
print(unique_list(a))

print('\n############################\n')

def f(integer):
    l = []
    for i in range(1,integer):
        if integer % i == 0:
            l.append(i)
    return l

a = 10
print(a)
print(f(a))

print('\n############################\n')

def find_biggest(s):
    l = s.split(' ')
    max = l[0] 
    for i in l:
        if len(i) > len(max):
            max = i        
    return max

string = 'python is an interpreter language'
print(string)
print(find_biggest(string))

print('\n############################\n')

def pascal(n):
    lst = []
    for i in range(0, n):
        lst2 = []
        lst.append(lst2)
        for j in range(0, i+1):
            lst[i].append('')
    for i in range(0 , n):
        for j in range(0, i+1):
            if j == 0:
                lst[i][j] = 1
            elif i == j:
                lst[i][j] = 1
            else:
                lst[i][j] = lst[i-1][j-1] + lst[i-1][j]
    
    for i in lst:
        for j in i:
            if j % 10:
                print(j, end = '   ')
            else:
                print(j, end = '  ')
        print()       
            

a = 6
print(a)
print('-----')
pascal(a)

print('\###########################\n')

def unique_code(lst):
    return set(lst)

a = [1, 2, 3, 1, 4, 2]
print(list(unique_code(a)))

print('\n############################\n')

def f(s):
    my_set = set()
    w = s.split(' ')
    for i in w:
        if i in my_set:
            return i
        else:
            my_set.add(i)

string = 'sara reza ali taha reza ali'
print(f(string))

print('\n############################\n')

def prime(n):
    lst = list()
    count = 0
    for i in range(2, n):
        for j in range(1, i+1):
            if i % j == 0:
                count += 1
        if count == 2:
            lst.append(i)
        count = 0
    return lst

print('\n############################\n')

n = 10
print(prime(n))

def magical(m):
    n = len(m[0])
    my_list = list()
    my_set = set()
    
    my_list.extend([sum(i) for i in m])
    
    count = 0 
    for i in range(0, n):
        for j in range(0, n):
            count += m[j][i]
        my_list.append(count)
        count = 0

    count1 = 0
    count2 = 0
    for i in range(0, n):   
        count1 += m[i][i]
        count2 += m[i][n-i-1]
    my_list.append(count1)
    my_list.append(count2)

    if len(set(my_list)) == 1:
        return True
    else:
        return False

m = [
    [2, 7, 6],
    [9, 5, 1],
    [4, 3, 8]
]

print(magical(m))

print('\n############################\n')

print('-----pep 484-----')
def greeting(name: str) -> str:
    '''
    saying hello to your name
    '''
    return 'hello' + name

print(greeting('Amirreza'))
print(greeting.__annotations__)
print(greeting.__doc__)

def add(x: int, y: int) -> int:
    '''
    add two number
    '''
    print(x + y)
add(2, 3)
print(add.__annotations__)
print(add.__doc__)
