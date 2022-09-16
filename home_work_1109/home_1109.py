import math
import random
def truncate(number, digits) -> float:
    nbDecimals = len(str(number).split('.')[1]) 
    if nbDecimals <= digits:
        return number
    stepper = 10**digits
    return math.trunc(stepper * number) / stepper
# Вычислить число π c заданной точностью d
# Пример:
# - при d = 0.001, π = 3.141   $10^{-1} ≤ d ≤10^{-10}$

print('1. Задача: вычислить число π c заданной точностью d')
d = int(input('Задайте сколько знаков после запятой вам нужно ---> '))
num_pi = math.pi
print(f'Число π, с исп.встроенной библиотеки python - math, с заданной вами точностью: {truncate(num_pi,d)}')
n = 1000
my_pi = sum(1/16**x*(4/(8*x + 1) - 2/(8*x + 4) - 1/(8*x + 5) - 1/(8*x + 6)) for x in range(n))
print(f'Число π, вычисленное с помощью формулы Бэйли — Боруэйна — Плаффа, с заданной вами точностью: {truncate(my_pi,d)}')
print()

# Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.

print('2.Задача: составить список простых множителей числа N')
n = int(input('Введите натуральное число ---> '))
def prost_mnogiteli(n):
    prost_mnogiteli = []
    for i in range(2,n+1):
        while n % i == 0:
            n = n/i
            prost_mnogiteli.append(i)
        i+=1  
    return prost_mnogiteli  
print(f'Список простых множителей числа {n} --> {prost_mnogiteli(n)}')
print()

# Задайте последовательность чисел. Напишите программу, которая выведет 
# список неповторяющихся элементов исходной последовательности.
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
print()

# Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100)
#  многочлена и записать в файл многочлен степени k.
# Пример:
# - k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0
print('4. Задача: Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена и записать в файл многочлен степени k')


def write_file(name,st):
    with open(name, 'w') as data:
        data.write(st)


def create_koef(k):
    spisok_koef = []
    for i in range(k+1):
        spisok_koef.append(round(random.uniform(0,101),2))
    return spisok_koef
    

def create_polinomial(sp):
    lst= sp[::-1]
    wr = ''
    if len(lst) < 1:
        wr = 'x = 0'
    else:
        for i in range(len(lst)):
            if i != len(lst) - 1 and lst[i] != 0 and i != len(lst) - 2:
                wr += f'{lst[i]}*x^{len(lst)-i-1}'
                if lst[i+1] != 0:
                    wr += ' + '
            elif i == len(lst) - 2 and lst[i] != 0:
                wr += f'{lst[i]}*x'
                if lst[i+1] != 0:
                    wr += ' + '
            elif i == len(lst) - 1 and lst[i] != 0:
                wr += f'{lst[i]} = 0'
            elif i == len(lst) - 1 and lst[i] == 0:
                wr += ' = 0'
    return wr

k = int(input("Введите натуральную степень k --> "))
koef = create_koef(k)
write_file('polinom.txt',create_polinomial(koef))

# Даны два файла, в каждом из которых находится запись многочлена. Задача - сформировать файл, содержащий сумму многочленов.
print('5. Задача: Даны два файла, в каждом из которых находится запись многочлена. Задача - сформировать файл, содержащий сумму многочленов')

write_file('polinom_1.txt','84*x^5 + 93*x^3 + 9*x^2 + 66*x - 45 = 0') 
write_file('polinom_2.txt','7*x^4 + 9*x^3 + 14*x^2 + 66*x + 5 = 0')

# нахожу степень многочлена (предполагаю, что многочлен в файле записан корректно, в порядке убывания степеней)
def pow_mn(k):
    if 'x^' in k:
        i = k.find('^')
        pow = int(k[i+1:])
        return pow
    else:
        if ('x' in k) and ('^' not in k):
            pow = 1
            return pow

with open('polinom_1.txt', 'r') as data:
    mn1 = data.readlines()
with open('polinom_2.txt', 'r') as data:
    mn2 = data.readlines()
print(f"Первый многочлен {mn1}")
print(f"Второй многочлен {mn2}")
st1 = mn1[0].replace(' ', '').replace('=0','').replace('-','+-')
koefs_st1 = []
koefs_st1 = st1.split('+')
koef_st1 = pow_mn(koefs_st1[0])
st2 = mn2[0].replace(' ', '').replace('=0','').replace('-','+-')
koefs_st2 = []
koefs_st2 = st2.split('+')
koef_st2 = pow_mn(koefs_st2[0])


def is_digit(n):
    try:
        int(n)
        return True
    except ValueError:
        return  False


# нахожу коэффициенты многочлена, в том числе 0

def find_koef(k, koeff): 
    lst = []
    i = 0
    s = pow_mn(k[0])
    while i < (len(k)):
        stroka = 'x^' + str(s)
        if stroka in k[i]:
            index = k[i].find('*')
            lst.append(int(k[i][:index]))
            i+=1
            s-=1
        elif ('x^' in k[i] and (stroka not in k[i])):
            lst.append(0)
            s-=1               
        elif 'x' in k[i]:
            index = k[i].find('*')
            lst.append(int(k[i][:index]))
            i+=1
            s-=1
        elif is_digit(k[i]):
            lst.append(int(k[i]))
            i+=1
    return lst

find_koeffs_st1 = find_koef(koefs_st1,koef_st1)
find_koeffs_st2 = find_koef(koefs_st2,koef_st2)

# нахожу коэффициенты суммы многочленов
def summ_mn(lst1,lst2):
    summ_koeff = []
    ii = len(lst1)
    jj = len(lst2)
    if ii == jj:
        for i in range(ii):
            summ_koeff.append(lst1[i] + lst2[i])
    elif ii > jj:
        for i in range(1,jj+1):
            summ_koeff.append(lst1[-i] + lst2[-i])
        for i in range(jj+1,ii+1):
            summ_koeff.append(lst1[-i])
    else:
        for i in range(1,ii):
            summ_koeff.append(lst1[-i] + lst2[-i])
        for i in range(ii+1,jj+1):
            summ_koeff.append(lst2[i])
    return(summ_koeff)
summ_koefs = summ_mn(find_koeffs_st1,find_koeffs_st2)
print('Сумма многочленов: ')
print(create_polinomial(summ_koefs))