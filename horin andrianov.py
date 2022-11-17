'''Лабораторная 7
Задание 1-2
import math
a = int(input("Введите значение a= "))
b = int(input("Введите значение b= "))
c = int(input("Введите значение c= "))
D = b ** 2 - 4 * a * c
if a == 0 and b == 0:
    print("Неразрешимое уравнение")
elif a == 0:
    print("Неквадратное уравнение")
elif D < 0:
  print("Случай комплексных корней")
elif b == 0 and c == 0:
    print("Нулевые корни: x1 = x2 = 0")
elif D > 0:
    x1 = (-b + math.sqrt(D)) / (2 * a)
    x2 = (-b - math.sqrt(D)) / (2 * a)
    print(x1)
    print(x2)
elif D == 0:
  x = -b / 2 * a
  print (x)
Задание 3

s1 = input("Строка 1: ")
s2 = input("Строка 2: ")
count = 0
ind = 1
while ind != -1:
    ind = s1.find(s2)
    if ind >= 0:
        count += 1
    s1 = s1[ind+1:]
print("Вывод:" + str(count))'''