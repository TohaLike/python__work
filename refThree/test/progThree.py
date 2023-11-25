'''
Created on 26 нояб. 2023 г.

@author: DD
'''
import math

def function_y(x, a, b):
    if x < 1.4:
        return math.pi * x**2 - 7/(x + 1)**2
    elif x ==  1.4:
        return a * (x - 2)**3 / 7 * math.sqrt(b * x)
    else:
        return x + 7 * math.sqrt(abs(x + a))
    
    
#
x = float(input("Введите значение x: "))
a = float(input("Введите значение a: "))
b = float(input("Введите значение b: "))
    
result = function_y(x, a, b)
print(f" x={x}, a={a}, b={b} y={result}")
    
    