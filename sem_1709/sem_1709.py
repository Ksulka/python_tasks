# 1. В файле находится N натуральных чисел, записанных через пробел. 
# Среди чисел не хватает одного, чтобы выполнялось условие A[i] - 1 = A[i-1]. Найдите это число.
# 1 2 3 5
with open('numbers.txt', 'r') as data:
    numbers = data.read().split()
lst_numbers = []
for i in range(len(numbers)):
    lst_numbers.append(int(numbers[i]))
print(numbers)
print(lst_numbers)


for i in range(len(lst_numbers)-1):
    if lst_numbers[i+1] - lst_numbers[i] !=1:
        index = i+1
        number = lst_numbers[i] + 1
       
lst_numbers.insert(index,number)    
print(f'В заданно последовательности не хватает {number}')
print(f' Новая последовательность {lst_numbers}')

# 2. Дан список чисел. Создайте список, в который попадают числа, 
# описываемые возрастающую последовательность. Порядок элементов менять нельзя. 
#     *Пример:* 
#     [1, 5, 2, 3, 4, 6, 1, 7] => [1, 5, 6, 7] и т.д.
lst =  [1, 5, 2, 3, 4, 6, 1, 7]   
new_list = [lst[0]]
max = lst[0]
for i in lst:
    if i > max:
        new_list.append(i)
        max = i
print(new_list)

# второе решение
res = [lst[0]]
[res.append(item) for item in lst if item > res[-1]]
print(res)

# 3. Напишите программу, удаляющую из текста все слова, содержащие "абв".
# 'Мы неабв очень любим Питон иабв Джавуабв!'
# 'Мы очень любим Питон!'
print (' '.join(filter(lambda x: not 'абв' in x,'Мы неабв очень любим Питон иабв Джавуабв!'.split())))

my_str = 'Мы неабв очень любим Питон иабв Джавуабв!'.split()
print(' '.join([word for word in my_str if 'абв' not in word]))
