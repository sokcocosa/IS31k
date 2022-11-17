a = int(input('Напиши a '))
b = int(input('Напиши b '))
c = int(input('Напиши c '))
print(a, '* x^2 +', b, '* x +', c, '= 0')
D = b ** 2 - 4 * a * c

if a == 0 and b == 0:
    print('Неразрешаемое уравнение')
elif a == 0:
    print('Неквадратное уравнение')
elif D > 0:
    x1 = (-b + D ** (1 / 2)) / (2 * a)
    x2 = (-b - D ** (1 / 2)) / (2 * a)
    print('x1 =', x1)
    print('x2 =', x2)
    print('Случай вещесвенных корней')
elif D == 0:
    x = (-b) / (2 * a)

    print('x2 = 0')
    print('Нулевые корни')
else:
    print("Случай комплексных корней")
