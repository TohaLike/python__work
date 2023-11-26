'''
Created on 26 нояб. 2023 г.

@author: DD
'''
import math

def function_y(x, a, b):
    if x < 3:
        return a / (math.exp(0.1 * x) + math.cos(x)**2)
    elif 3 <= x < 1:
        return (a + b) /  math.log(x + 1)
    elif x >= 10:
        return abs(math.sin(x))
        
#
x = float(input("Введите значение x: "))
a = float(input("Введите значение a: "))
b = float(input("Введите значение b: "))

result = function_y(x, a, b)
print(f" x={x} a={a} b={b} result={result}")
