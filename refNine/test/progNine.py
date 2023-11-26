'''
Created on 26 нояб. 2023 г.

@author: DD
'''
import math

def function_y(x, a, b):
    if x > 1:
        return a * math.log(x) + x**(1/3)
    elif x == 1:
        return 2 * a * math.cos(x) + 3**2
    else:
        return (a + 5) / math.log(x-1)**2
    
    
#
x = float(input("Введите значение x: "))
a = float(input("Введите значение a: "))
b = float(input("Введите значение b: "))
    
result = function_y(x, a, b)
print(f" x={x}, a={a}, b={b} y={result}")
