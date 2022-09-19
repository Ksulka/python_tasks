import random
# 1. Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
#     *Пример:*
#     - 0,56 -> 11

# # старое решение
num = float(input("1. Введите вещественное число, вещественная часть отделяется точкой или запятой --> "))    
str_num = str(num)
str_sum = str_num.replace('.','').replace(',','').replace('-','')
summ = 0
for i in range(len(str_sum)):
    summ += int(str_sum[i])
print(f'Сумма цифр введенного числа равна: {summ}')

# # новое решение
number = input("1. Введите вещественное число, вещественная часть отделяется точкой или запятой --> ")
res = sum(map(int,list(number.replace('.', '').replace(',','').replace('-',''))))
print(f'Сумма цифр введенного числа равна: {res}')



# 2. Задайте список из n чисел последовательности (1 + 1/n)^n и выведите на экран их сумму.

# Старое решение 
n = int(input('Введите число N для создания последовательности --> '))
lst = []
for i in range(1,n+1):
    lst.append(round((1+1/i)**i,2))
    i+=1
print(lst)
summ = 0
for i in range(len(lst)):
    summ += lst[i]
print(f'Сумма значений последовательности равна: {summ}')

# новое решение:
def f(x):
    return (1+1/x)**x
lst = [f(i) for i in range(1,n+1)]
print(f'Сумма значений последовательности равна: {sum(lst)}')


# 3. Задайте последовательность чисел. Напишите программу, которая выведет 
# список неповторяющихся элементов исходной последовательности.

# старое решение:
def spisok_int(n: int):
    list = []
    for i in range(n):
        list.append(random.randrange(0,10))
    return list

def spisok_bez_povtorov(list):
    spisok_new = []
    [spisok_new.append(i) for i in list if list.count(i)==1]
    spisok_new.sort()
    return spisok_new

n = int(input('введите количество элементов в исходном списке (чем больше эл-тов, тем больше повторов) --> '))
spisok_s_povtorami = spisok_int(n)
print(f'Начальный список: {spisok_s_povtorami}')
print(f'Список уникальных элементов: {spisok_bez_povtorov(spisok_s_povtorami)}')

# новое решение:
lst_for_sort = [random.randint(0,10) for i in range(int(input('Введите количество элементов --> ')))]
lst_unic = []
[lst_unic.append(i) for i in lst_for_sort if lst_for_sort.count(i)==1]
print(f'Начальный список: {lst_for_sort}')
print(f'Список уникальных элементов: {lst_unic}')

# 4. Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.
# Пример:
# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

# старое решение

def spisok_int(n: int):
    list = []
    for i in range(n):
        list.append(random.randrange(0,100))
    return list

def sum_odd(list):
    sum = 0
    for i in range(1,len(list),2):
        sum += list[i]
    return sum

k = int(input('Введите количество элементов --> '))
list_for_summ_odd = spisok_int(k)
print(f'Список из {k} элементов: {list_for_summ_odd}')
print(f'Сумма эл-тов на нечетных позициях: {sum_odd(list_for_summ_odd)}')


# новое решение:

lst_ = [random.randint(0,10) for i in range(int(input('Введите количество элементов --> ')))]
print(lst_)
print(f'Сумма эл-то на нечетных позициях: {sum_odd(lst_)}')