'''
Created on 26 нояб. 2023 г.

@author: DD
'''
import math

def function_y(x, a, b):
    if x < math.pi / 2:
        return 1 / x**3
    elif math.pi / 2 <= x <= math.pi:
        return b * x - math.sin(x)**2
    else:
        return 1 / (a * math.exp(x))
    
    
#
x = float(input("Введите значение x: "))
a = float(input("Введите значение a: "))
b = float(input("Введите значение b: "))
    
result = function_y(x, a, b)
print(f" x={x}, a={a}, b={b} y={result}")
    
    