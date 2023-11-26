'''
Created on 26 нояб. 2023 г.

@author: DD
'''

import math

def function_y(x, a, b, c):
    if c > 0:
        return (a + b) / c - math.sin(2 * x + c)**3
    elif c <= 0 and a > b:
        return math.log(x + 2 * c) - (a - b * c)**(1/3)
    else:
        1 / math.tan(a * c / x) + 2 * x * b
        
#
x = float(input("Введите число x: "))
a = float(input("Введите число a: "))
b = float(input("Введите число b: "))
c = float(input("Введите число c: "))

result = function_y(x, a, b, c)
print(f"x={x}, a={a}, b={b}, c={c}, y={result}")

