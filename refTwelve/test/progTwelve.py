'''
Created on 26 нояб. 2023 г.

@author: DD
'''
import math

def function_y(x, a, b):
    if (a < b):
        return b / (0.4 * 5**x + math.sin(x)**2)
    elif a > b:
        return (a + b) / math.log(a - b) + x
    elif a == b:
        return abs(math.sin(x)**3)
    
#
x = float(input("Введите число x:"))
a = float(input("Введите число a:"))
b = float(input("Введите число b:"))

result = function_y(x, a, b)
print(f"x={x}, a={a}, b={b}, y={result}")