'''
Created on 26 нояб. 2023 г.

@author: DD
'''
import math

def function_y(x, a, b, c):
    if a > 0 and c > 0:
        return a * c - x * math.sin(x**3 / c * a**2)
    elif a != 0 and b != 0:
        return math.log((a * c * x)**3, 5) + x**2 + c / (a * b)
    else:
        return (a * x - c * math.sin(b * x - c))**(1 / 3)
#
x = float(input("Введите значение x: "))
a = float(input("Введите значение a: "))
b = float(input("Введите значение b: "))
c = float(input("Введите значение c: "))

result = function_y(x, a, b, c)

print(f"x={x}, a={a}, b={b}, c={c}, y={result}")

    
        