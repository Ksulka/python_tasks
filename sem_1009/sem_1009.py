# 1. Реализуйте алгоритм задания случайных чисел без использования встроенного генератора псевдослучайных чисел.
import time
def randnum(minn,maxx):
    time.sleep(0.3)
    return int((time.time() % 1  * (maxx+1 - minn)) + minn)

for i in range(10):
    print(randnum(0,10))

# 2. Задайте список. Напишите программу, которая определит, присутствует ли в заданном списке строк некое число.
# ['efg23', '79234gefg', 'sdgs', 'g53']
# '2'
# ['efg23', '79234gefg']

def check_p_in_list(list, p):
    count = 0
    new_list = []
    for i in list:
        if p in i:
            new_list.append(i)
    return new_list
    

list = ['efg23', '79234gefg', 'sdgs', 'g53']
p = '2'
print(check_p_in_list(list, p))



# 3. Напишите программу, которая определит позицию второго вхождения 
# строки в списке либо сообщит, что её нет.

# *Пример:*

# - список: ["qwe", "asd", "zxc", "qwe", "ertqwe"], ищем: "qwe", ответ: 3
# - список: ["йцу", "фыв", "ячс", "цук", "йцукен", "йцу"], ищем: "йцу", ответ: 5
# - список: ["йцу", "фыв", "ячс", "цук", "йцукен"], ищем: "йцу", ответ: -1
# - список: ["123", "234", 123, "567"], ищем: "123", ответ: -1
# - список: [], ищем: "123", ответ: -1


def findstr(my_list: list, find_string: str) -> int:
    count = 0
    for i in range(len(my_list)):
        if find_string == my_list[i]:
            count += 1
            if count == 2:
                return i
    return -1

list_find = ["йцу", "фыв","йцу", "ячс", "цук", "йцукен"]
find_string = "йцу"

print(f'Позиция второго вхождения:  {findstr(list_find, find_string)}')
