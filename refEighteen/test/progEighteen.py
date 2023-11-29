'''
Created on 29 нояб. 2023 г.

@author: DD
'''

a = float(input("Введите длину кирпича a: "))
b = float(input("Введите длину кирпича b: "))
c = float(input("Введите длину кирпича c: "))

x = float(input("Введите ширину отверстия x: "))
x = float(input("Введите высоту отверстия y: "))


result = print("Кирпич войдёт в отверстие")

def function_nums(a, b, c, x, y):
    if  (a <= x and b <= y) or (a <= y and b <= x) or \
        (b <= x and c <= y) or (b <= y and c <= x) or \
        (a <= x and c <= y) or (a <= y and c <= x):
        
        print("Кирпич войдёт в отверстие")
    else:
        print("Кирпич не войдёт в отверстие")

    
        