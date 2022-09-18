# 1. Напишите программу вычисления арифметического выражения заданного строкой. 
# Используйте операции +,-,/,*. приоритет операций стандартный. 
#     *Пример:* 
#     2+2 => 4; 
#     1+2*3 => 7; 
#
#     - Добавьте возможность использования скобок, меняющих приоритет операций.
#         *Пример:* 
#         1+2*3 => 7; 
#         (1+2)*3 => 9;

import re
import random
expr = input('Введите выражение, используя операции +,-,/,* => ')
print(eval(expr))

OPERATORS = {'+': (1, lambda x, y: x + y), '-': (1, lambda x, y: x - y),
             '*': (2, lambda x, y: x * y), '/': (2, lambda x, y: x / y)}
def eval_(formula_string): 

    def parse(formula_string):#Парсер исходной строки
        number = ''
        for s in formula_string:
            if s in '1234567890.': # если символ - цифра, то собираем число
                number += s  
            elif number: # если символ не цифра, то выдаём собранное число и начинаем собирать заново
                yield float(number) 
                number = ''
            if s in OPERATORS or s in "()": # если символ - оператор или скобка, то выдаём как есть
                yield s 
        if number:  # если в конце строки есть число, выдаём его
            yield float(number) 

    def shunting_yard(parsed_formula):#Алгоритм сортировочной станции
        stack = []  # в качестве стэка используем список
        for token in parsed_formula:
            # если элемент - оператор, то отправляем дальше все операторы из стека, 
            # чей приоритет больше или равен пришедшему,
            # до открывающей скобки или опустошения стека.
            # здесь мы пользуемся тем, что все операторы право-ассоциативны
            if token in OPERATORS: 
                while stack and stack[-1] != "(" and OPERATORS[token][0] <= OPERATORS[stack[-1]][0]:
                    yield stack.pop()
                stack.append(token)
            elif token == ")":
                # если элемент - закрывающая скобка, выдаём все элементы из стека, до открывающей скобки,
                # а открывающую скобку выкидываем из стека.
                while stack:
                    x = stack.pop()
                    if x == "(":
                        break
                    yield x
            elif token == "(":
                # если элемент - открывающая скобка, просто положим её в стек
                stack.append(token)
            else:
                # если элемент - число, отправим его сразу на выход
                yield token
        while stack:
            yield stack.pop()

    def calc(polish):#Вычислитель
        stack = []
        for token in polish:
            if token in OPERATORS:  # если приходящий элемент - оператор,
                y, x = stack.pop(), stack.pop()  # забираем 2 числа из стека
                stack.append(OPERATORS[token][1](x, y)) # вычисляем оператор, возвращаем в стек
            else:
                stack.append(token)
        return stack[0] # результат вычисления - единственный элемент в стеке
    return calc(shunting_yard(parse(formula_string))) 
print(eval_(expr))
#     - Добавьте возможность использования скобок, меняющих приоритет операций.
        
#         *Пример:* 
        
#         1+2*3 => 7; 
        
#         (1+2)*3 => 9;
        

# 2. Дана последовательность чисел. Получить список уникальных элементов заданной последовательности.

# *Пример:* 

# [1, 2, 3, 5, 1, 5, 3, 10] => [2, 10]
print('3. Задача: задать последовательность чисел и вывести список неповторяющихся элементов исходной последовательности')
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
# способ с лямбда и фильтром
print(tuple(filter(lambda num: spisok_s_povtorami.count(num) == 1, spisok_s_povtorami)))
