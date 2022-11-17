print('Написать программу решения квадратного уравнения ax^2 + bx + c = 0')
a = float(input())
b = float(input())
c = float(input())

disc = b ** 2 - 4 * a * c
print('Дискриминант D = ' + str(disc))
if disc > 0:
    x1 = (-b + disc ** 0.5) / (2 * a)
    x2 = (-b - disc ** 0.5) / (2 * a)
    print('x1 = ' + str(x1))
    print('x2 = ' + str(x2))
elif disc == 0:
    x = -b / (2 * a)
    print('x = ' + str(x))
else:
    print('Корней нет')
