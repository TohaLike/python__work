'''
Created on 28 нояб. 2023 г.

@author: DD
'''

a = float(input("Введите число: "))
b = float(input("Введите число: "))
c = float(input("Введите число: "))

if a + b + c < 10:
    minNum = min(a, b, c)
    if min == a:
        a = (b + c)
    elif min == b:
        b = (a + c)
    else:
        mainMinNum = min(a, b)
        if mainMinNum == a:
            a = (b + c) 
        else:
            b = (a + c)
            
print(f"После замены: a={a}, b={b}, c={c}")
