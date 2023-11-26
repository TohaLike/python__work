'''
Created on 26 нояб. 2023 г.

@author: DD
'''

import math

def function_y(x, a, b, c):
    if a > 0 and b > 0 and c > 0:
        return (a * x**3) / abs(c**2 + b * x) - math.cos(a * x + b)
    elif c < 0 and b < 0:
        return math.log(3 * x + c) + (a * b * x)**(1/3)
    else:
        return (a * x + c * b)**3 + math.cos(a * b * x)**2
#

x = float(input("Введите число x: "))
a = float(input("Введите число a: "))
b = float(input("Введите число b: "))
c = float(input("Введите число c: "))

result = function_y(x, a, b, c)

print(f"x={x}, a={a}, b={b}, c={c}, y={result}")
