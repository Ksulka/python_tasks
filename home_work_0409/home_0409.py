# 1. Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
    
#     *Пример:*

#     - 0,56 -> 11
print()
num = float(input("1. Введите вещественное число, вещественная часть отделяется точкой --> "))    
str_num = str(num)
str_sum = str_num.replace('.','')
sum = 0
for i in range(len(str_sum)):
    sum += int(str_sum[i])
print(f'Сумма цифр введенного числа равна: {sum}')
print()

# 2. Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
    
#     *Пример:*
    
#     - пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)
def fact(n):
    if n==1:
        return 1
    else:
        return n * fact(n-1)   
n = int(input('2. Введите натуральное число N --> '))    
factorial = []
for i in range(1,n+1):
    factorial.append(fact(i))
print(factorial)
print()

# 3. Задайте список из n чисел последовательности (1 + 1/n)^n и выведите на экран их сумму.
n = int(input('3. Введите число N для создания последовательности --> '))
list = []
for i in range(1,n+1):
    list.append(round((1+1/i)**i,2))
    i+=1
print(list)
sum = 0
for i in range(len(list)):
    sum += list[i]
print(f'Сумма значений последовательности равна: {sum}')
print()

# 4. Задайте список из N элементов, заполненных числами из промежутка [-N, N].
# Найдите произведение элементов на указанных пользователем через пробел позициях. 
import random
k = int(input('Введите количество элементов: N --> '))
numbers = []
for i in range(k):
    numbers.append(random.randrange(-k,k))
print(numbers)
pos = input('Введите позиции элементов, которые нужно перемножить, разделяя их через пробел, в промежутке от 0 до (N-1) --> ')

list_pos = pos.split()
print(list_pos)
mult = 1
for i in range(len(list_pos)):
    mult = mult * numbers[int(list_pos[i])]
    i+=1
print(f'Произведение выбранных элементов равно: {mult}')
print()

# Реализуйте алгоритм перемешивания списка 
print(' 5. Алгоритм перемешивания списка.')
list = [1, 2, 3, 4, 5, 6]
print(f'Не перемешанный список: {list}')
list = random.sample(list,len(list))
print(f'Перемешанный список: {list}')
# Или так:
random.shuffle(list)
print(f'Перемешанный список №2: {list}')