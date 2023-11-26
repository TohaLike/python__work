'''
Created on 26 нояб. 2023 г.

@author: DD
'''
import math

def function_y(x, a, b):
    if x > a:
        return x * math.sqrt(x - a)
    elif x == a:
        return x / math.sin(a * x)
    else:
        return math.exp(-a*x) * math.cos(a * x)
    
    
#
x = float(input("Введите значение x: "))
a = float(input("Введите значение a: "))
b = float(input("Введите значение b: "))
    
result = function_y(x, a, b)
print(f" x={x}, a={a}, b={b} y={result}")
