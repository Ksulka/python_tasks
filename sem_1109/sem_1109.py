from math import *

# Задайте строку из набора чисел. Напишите программу, которая покажет большее и меньшее число. 
# В качестве символа-разделителя используйте пробел.
user_string = input('Введите числа через пробел --> ').split()
numbers = list(map(int, user_string))
print(numbers)
print(max(numbers), min(numbers))



# Найдите корни квадратного уравнения Ax² + Bx + C = 0 двумя способами: 
# 1) с помощью математических формул нахождения корней квадратного уравнения 
# 2) с помощью дополнительных библиотек Python
def diskrimenant(a,b,c):
    diskr = b**2 - 4*a*c
    if  diskr < 0:
        x = 'Уравнение не имеет решения'
        return x
    elif diskr == 0:
        x = -b/(2*a)
        return x
    elif diskr > 0:
        x_1 = (-b + sqrt(diskr))/(2*a)
        x_2 = (-b - sqrt(diskr))/(2*a)
        return x_1, x_2

a = float(input('Введите старший коэффициент A --> '))
b = float(input('Введите второй коэффициент B --> '))
c = float(input('Введите свободный член С --> '))

print(f'Ответ: {diskrimenant(a,b,c)}')

# Задайте два числа.
# Напишите программу, которая найдёт НОК (наименьшее общее кратное) этих двух чисел.
def nok(a,b):
    nok = min(a, b)
    while True:
        if nok % a==0 and nok % b==0:
            break
        nok += 1
    return nok

def NOD(a,b):
    while True:
        if a > b:
            a = a - b
        else:
            b = b - a

        if a % b == 0:
            return b
        elif b % a == 0:
            return a


def NOK(a:int, b:int) -> int:
        return int((a * b) / NOD(a,b))

a = int(input("Введите первое число --> "))
b = int(input("Введите второе число --> "))
print(f'Наименьшее общее кратное: {nok(a,b)}')
print(f'Наименьшее общее кратное: {NOK(a, b)}')
