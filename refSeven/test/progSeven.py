'''
Created on 26 нояб. 2023 г.

@author: DD
'''
import math

def function_y(x, a):
    if x < 1.3:
        return math.pi**2 - 7 / math.sqrt(x)
    elif x == 1.3:
        return a * x**3 + 7 * math.sqrt(x)
    else:
        return function_y2(x, a)
       

def function_y2(x, a):
    if  x > 7 * math.sqrt(x):
        return math.log(x - 7 * math.sqrt(x))
    else: return None
#

x = float(input("Введите значение x: "))
a = float(input("Введите значение a: "))
    
result = function_y(x, a)

print(f" x={x}, a={a}, y={result}")
