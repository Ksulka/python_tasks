import random
def spisok_int(n: int):
    list = []
    for i in range(n):
        list.append(random.randrange(0,100))
    return list

def spisok_float(n: int):
    list = []
    for i in range(n):
        list.append(round(random.uniform(0,100),2))
    return list

def sum_odd(list):
    sum = 0
    for i in range(1,len(list),2):
        sum += list[i]
    return sum

def multi(list):
    new_list = []
    if len(list) % 2:
        for i in range(len(list)//2 + 1):
            new_list.append(list[i]*list[len(list)-1-i])
        return new_list
    else:
        for i in range(len(list)//2):
            new_list.append(list[i]*list[len(list)-1-i])
        return new_list

def diff_min_max_float(list):
    new_list = []
    for i in range(len(list)):
        new_list.append(round(list[i] % 1, 2))
    diff = max(new_list) - min(new_list)
    return diff

def dec_in_bin(dec):
    list_mod = []
    bin_num = ''
    while dec != 0:
        list_mod.append(dec % 2)
        dec = dec // 2 
    for i in range(len(list_mod)):
        bin_num += str(list_mod[len(list_mod)- i - 1])
    return bin_num

def fib(n):
    if n == 0:
        return 0
    if n in [1,2]:
        return 1
    else:
        return fib(n-1) + fib(n-2)

# Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.
# Пример:
# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12
print('1. Задача: задать список и найти сумму элементов, стоящих на нечетных позициях')
k = int(input('Введите количество элементов --> '))
list_for_summ_odd = spisok_int(k)
print(f'Список из {k} элементов: {list_for_summ_odd}')
print(f'Сумма эл-тов на нечетных позициях: {sum_odd(list_for_summ_odd)}')
print()

# Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Пример:
# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]
print('2. Задача: найти произведение пар списка')
n = int(input('Введите кол-во элементов списка --> '))
list_multi = spisok_int(n)
print(f'Список из {n} элементов: {list_multi}')
print(f'Произведение пар: {multi(list_multi)}')
print()

# Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным
#  и минимальным значением дробной части элементов.
# Пример:
# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19
print('3. Задача: задать список из вещ.эл-тов. Найти разницу между максимальным и минимальным значением дробной части')
n = int(input('Введите кол-во элементов в списке: --> '))
list_for_float = spisok_float(n)
print(f'Список вещественных элементов: {list_for_float}')
print(f'Разница между максимальным и минимальным значением дробной части: {diff_min_max_float(list_for_float)}')
print()

# Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# Пример:
# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10
print('4. Задача: преобразовать десятичное число в двоичное')
dec_num = int(input('Введите десятичное число --> '))
print(f' {dec_num} в двоичной системе счисления --> {dec_in_bin(dec_num)}')
print()

# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
# Пример:
# - для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21] 
print('5. Задача: составить список чисел Фибоначчи, в том числе для отрицательных индексов')
f = int(input('Введите сколько чисел Фиббоначи с положительными индексами вы хотите: -->  '))
fib_list = []
for i in range(f+1):
    fib_list.append(fib(i))
for i in range(1,f):
    if i % 2 == 0:
        fib_list.insert(0,-fib(i))
    else:
        fib_list.insert(0,fib(i))
print(f'Список чисел Фибоначчи, в том числе для отрицательных индексов: {fib_list}')