'''
Created on 26 нояб. 2023 г.

@author: DD
'''
import math

def function_y(x, a, b):
    if x < 0.5:
        return (b + x**2) / math.sqrt(x + a)
    elif x == 0.5:
        return (b + 1) * math.sqrt(x + a)
    else:
        return math.cos(x + b) * math.sin(x)**2
    
    
#
x = float(input("Введите значение x: "))
a = float(input("Введите значение a: "))
b = float(input("Введите значение b: "))
    
result = function_y(x, a, b)
print(f" x={x}, a={a}, b={b} y={result}")
