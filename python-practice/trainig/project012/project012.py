def factorial(n: int) -> int:
    '''
    Factorial calculation
    '''
    if n == 1 or n == 0:
        return 1
    else:
        return n * factorial(n-1)

number = 5
print(factorial(number))
print(factorial.__annotations__)
print(factorial.__doc__)

print('\n####################\n')

def multiply(num1: int, num2: int) -> int:
    '''
    Multiplying two numbers
    '''
    if num2 == 0:
        return 0
    elif num2 == 1:
        return num1
    else:
        return num1 + multiply(num1, num2-1)

num1 = 2
num2 = 3
print(multiply(num1, num2))

print('\n####################\n')

from typing import Union

def multiply(num1: Union[int, float], num2: Union[int, float]) -> Union[float, int]:
    '''
    Multiplying two numbers with union hint
    '''
    if num2 == 0:
        return 0
    elif num2 == 1:
        return num1
    else:
        return num1 + multiply(num1, num2-1)

print(multiply(3.0, 4.0))
print(multiply(3, 4))

print('\n####################\n')

def power(num1: int, num2: int) -> int:
    '''
    Implementation of power function
    '''
    if num2 == 0:
        return 1
    else:
        if num2 == 1:
            return num1
        else:
            return num1 * power(num1, num2-1)

print(power(2, 3))
print(power(2, 0))
print(pow(0, 3))

print('\n####################\n') 

def fibonachi(number: int | float) -> int:
    lst = list()
    a = 0
    b = 1
    while a < number:
        lst.append(a)
        a, b = b, a+b
    return lst

print(fibonachi(10.1))

print('\n####################\n') 

def fibonachi_rec(number: int | float) -> int:
    if number == 0:
        return 0
    elif number == 1:
        return 1
    else:
        return fibonachi_rec(number-1) + fibonachi_rec(number-2)
    
print(fibonachi_rec(10))

print('\n####################\n') 

def sum_list(lst: list, n: int) -> int:
    '''
    Summing list elements
    '''
    if n == 0:
        return lst[0]
    else:
        return lst[n] + sum_list(lst, n-1)


a = [2, 4, 5, 6, 7]
print(sum_list(a , len(a)-1))

print('\n####################\n') 

def sum_list(lst: list) -> int:
    '''
    obtimized Summing list elements
    '''
    if len(lst) == 1:
        return lst[0]
    else:
        return lst[0] + sum_list(lst[1:])


a = [2, 4, 5, 6, 7]
print(sum_list(a ))

print('\n####################\n') 

def sum_digits(number: int) -> int:
    '''
    summing digits of the number
    '''
    if number == 0:
        return 0
    else:
        return sum_digits(number//10) + number % 10

print(sum_digits(123)) 

print('\n####################\n') 

def reverse_number(number: int) -> int:
    '''
    reverse number 
    '''
    if number < 10:
        return number
    else:
        return number % 10 * 10 ** (len(str(number))-1) + reverse_number(number//10)


print(reverse_number(123)) 

print('\n####################\n') 

def sequance(number: int) -> int:
    if number < 1:
        return 0
    else:
        return number + sequance(number-2)
    
print(sequance(9))

print('\n####################\n') 

def base_convert(number: int, base: int) -> str:
    s = '0123456789ABCDEF'
    if number < base:
        return s[number]
    else:
        return base_convert(number//base , base) + s[number%base]

print(base_convert(8,2))       
        
print('\n####################\n')

def binary_search(lst: list, number: int, start: int, end: int) -> Union[int, bool]:
    if start > end:
        return False
    mid = (start + end) // 2
    if number == lst[mid] :
        return mid
    elif number > lst[mid] :
        return binary_search(lst, number, mid+1, end)
    else:
        return binary_search(lst, number, start, mid-1)



a = [2, 4, 7, 12, 19, 25, 37]
print(binary_search(a, 25, 0, len(a)-1))

        
        