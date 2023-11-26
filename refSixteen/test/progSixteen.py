'''
Created on 26 нояб. 2023 г.

@author: DD
'''
import math

def function_y(x, a, b, c):
    if b > 0:
        return a * x**3 - math.tan(c * x**3 / b)
    elif a != 0 and b != 0: 
        return math.sin(a * x**3) + x**math.log(5) + c / (a**2 * b)
    else:
        return (a*x - b*x - c)**(1/3) + 5*x / 12
    
#

x = float(input("Введеите число x: "))
a = float(input("Введеите число a: "))
b = float(input("Введеите число b: "))
c = float(input("Введеите число c: "))

result = function_y(x, a, b, c)

print(f"x={x}, a={a}, b={b}, c={c}, y={result}")
