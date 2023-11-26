'''
Created on 26 нояб. 2023 г.

@author: DD
'''
import math

def function_y(x, a, b):
    if x < 2:
        return (a + b) / (math.exp(x) + math.cos(x))
    elif 2 <= x < 8:
        return a / (b * x + 1)
    else:
        return math.exp(x) + math.sin(2 * x)
    
    
#
x = float(input("Введите значение x: "))
a = float(input("Введите значение a: "))
b = float(input("Введите значение b: "))
    
result = function_y(x, a, b)
print(f" x={x}, a={a}, b={b} y={result}")
