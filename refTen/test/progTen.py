'''
Created on 26 нояб. 2023 г.

@author: DD
'''
import math

def function_y(x, a):
    if x < 2:
        return 1 / math.log(x + 1)
    elif x > 2:
        return 2 * math.sin(x**2 * math.sqrt(abs(a * x)))
    elif x == 2:
        return a * x**3
 
#
x = float(input("Введите значение x: "))
a = float(input("Введите значение a: "))
    
result = function_y(x, a)
print(f" x={x}, a={a}, y={result}")
