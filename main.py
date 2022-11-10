#Вариант 12 Хайдаров Разиль, Рустамов Осман


def oprdelitil_3x3(list1):
    try:
        return list1[0][0] * list1[1][1] * list1[2][2] + list1[0][1] * list1[1][2] * list1[2][0] + list1[0][2] * list1[1][0] * list1[2][1] - \
               list1[2][0] * list1[1][1] * list1[0][2] - list1[2][1] * list1[1][2] * list1[0][0] - list1[2][2] * list1[1][0] * list1[0][1]
    except IndexError:
        return "Нужна матрица 3x3"


def opredelitil_2x2(list1):
    try:
        return list1[0][0] * list1[1][1] - list1[0][1] * list1[1][0]
    except IndexError:
        return "Нужна матрица 2x2"


numb = int(input())
list1 = []
if numb == 3:
    for i in range(3):
        list1.append(list(map(int, input().split())))
        print(list1)
    print(oprdelitil_3x3(list1))
elif numb == 2:
    for i in range(2):
        list1.append(list(map(int, input().split())))
    print(opredelitil_2x2(list1))
