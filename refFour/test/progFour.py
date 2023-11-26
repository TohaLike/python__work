'''
Created on 26 нояб. 2023 г.

@author: DD
'''
import math

def function_y(x, a, b):
    if x < 1:
        return 5 * b * math.cos(x)**2
    elif x == 1:
        return 1.8/(a * x)
    elif 1 < x < 2:
        return (x - 1)**2 + 6
    else:
        return 3 * math.tan(x)
    
    
#
x = float(input("Введите значение x: "))
a = float(input("Введите значение a: "))
b = float(input("Введите значение b: "))
    
result = function_y(x, a, b)
print(f" x={x}, a={a}, b={b} y={result}")
