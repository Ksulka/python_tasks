# Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.

# Пример:

# - 6 -> да
# - 7 -> да
# - 1 -> нет

week_day = int(input('Введите цифру, обозначающую день недели -->  '))
if (week_day == 6) or (week_day == 7):
    print("Этот день выходной")
else: 
    print("Это будний день")


# Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.
def true_table(x, y, z):
    return (not (x or y or z)) == (not x and not y and not z)
if (true_table(0, 0, 0) and true_table(0, 0, 1) and true_table(0, 1, 0) and 
true_table(0, 1, 1) and true_table(1, 0, 0) and true_table(1, 0, 1) and
true_table(1, 1, 0) and true_table(1, 1, 1)):
    print("Проверка истинности утверждения прошла успешно для всех значений предикат")
else:
    print("Ложно")





# Напишите программу, которая принимает на вход координаты точки (X и Y), причём X ≠ 0 и Y ≠ 0 и 
# выдаёт номер четверти плоскости, в которой находится эта точка (или на какой оси она находится).

# Пример:

# - x=34; y=-30 -> 4
# - x=2; y=4-> 1
# - x=-34; y=-30 -> 3

x = float(input("Введите Х координату, но ≠ 0 -->  "))
y = float(input("Введите Y координату, но ≠ 0 -->  "))

if ((x > 0) and (y > 0)):
    print("Точка с такими координатами находится в ПЕРВОЙ ЧЕТВЕРТИ  ")
elif ((x < 0) and (y > 0)):
    print("Точка с такими координатами находится во ВТОРОЙ ЧЕТВЕРТИ  ")
elif ((x < 0) and (y < 0)):
    print("Точка с такими координатами находится в ТРЕТЬЕЙ ЧЕТВЕРТИ  ")
else:
    print("Точка с такими координатами находится в ЧЕТВЕРТОЙ ЧЕТВЕРТИ  ")

# Напишите программу, которая по заданному номеру четверти, показывает
#  диапазон возможных координат точек в этой четверти (x и y).
n = int(input("Введите номер четверти -- >  "))
if (n == 1):
    print("В первой четверти координаты точки могут быть в таких диапазонах: X > 0  и  Y > 0  ")
elif (n==2):
    print("Во второй четверти координаты точки могут быть в таких диапазонах: X < 0  и  Y > 0  ")
elif (n==3):
    print("В Третьей четверти координаты точки могут быть в таких диапазонах: X < 0  и  Y < 0  ")
elif (n==4):
    print("В четвертой четверти координаты точки могут быть в таких диапазонах: X > 0  и  Y < 0  ")

# Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.

# Пример:

# - A (3,6); B (2,1) -> 5,09
# - A (7,-5); B (1,-1) -> 7,21

x_1 = float(input("Ввведите координату Х первой точки -->  "))
y_1 = float(input("Ввведите координату Y первой точки -->  "))
x_2 = float(input("Ввведите координату Х второй точки -->  "))
y_2 = float(input("Ввведите координату Y второй точки -->  "))

print(f"Расстояние между точками равно {round(((abs(x_1 - x_2))**2 + (abs(y_1 - y_2))**2)**0.5,2)}")