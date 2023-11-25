'''
Created on 26 нояб. 2023 г.

@author: DD
'''
import math

def function_y(x, a, b):
    if x < 3:
        return math.pi * x**2 - 5/x**2
    elif x == 3:
        return a * x**3 + b * math.sqrt(x)
    else:
        return math.log(x + math.sqrt(x + a))
    
    
#
x = float(input("Введите значение x: "))
a = float(input("Введите значение a: "))
b = float(input("Введите значение b: "))
    
result = function_y(x, a, b)
print(f" x={x}, a={a}, b={b} y={result}")
    
    
    