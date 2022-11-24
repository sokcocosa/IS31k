import math


class Square_eduation:
    pass


def square_ed(a, b, c):
    discr = b ** 2 - 4 * a * c
    if a == 0 and b == 0:
        return "Неразрешимое уравнение"
    elif a == 0:
        return "Неквадратное уравнение"
    elif discr < 0:
        return "Случай комплексных чисел"
    elif b == 0 and c == 0:
        return "x1 = x2 = 0"
    else:
        if discr > 0:
            x1 = (-b + math.sqrt(discr)) / (2 * a)
            x2 = (-b - math.sqrt(discr)) / (2 * a)
            return "x1 = " + str(x1) + "  ;  x2 = " + str(x2)
        elif discr == 0:
            x = -b / (2 * a)
            return "x = " + str(x)
