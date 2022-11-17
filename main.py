from math import sqrt


def work7__1_2():
    a, b, c = map(int, input("Введите три числа через пробел: ").split())
    D = b ** 2 - 4 * a * c

    if not a and not b:
        print("Неразрешимое уравнение")
    elif not a:
        print("Неквадратное уравнение")
    elif D < 0:
        print("Случай комплексных корней")
    elif not b and not c:
        print("Нулевые корни: x1 = x2 = 0")
    elif D > 0:
        x1 = (-b + sqrt(D)) / (2 * a)
        x2 = (-b - sqrt(D)) / (2 * a)
        print(f"x1: {x1}\nx2: {x2}")
    elif not D:
        x = -b / 2 * a


def work7__2():
    s1, s2 = map(str, input("Введите две строки через пробел: ").split())

    count = 0
    ind = 1
    while ind != -1:
        ind = s1.find(s2)
        if ind >= 0:
            count += 1
        s1 = s1[ind + 1:]
    print(f"Вывод: {str(count)}")


def work8__1_2():
    ...


def work8__2():
    ...


if __name__ == '__main__':
    variant = input("Введите вариант(7-8): ")
    match variant:
        case "7":
            work = input("Введите задание(1-3): ")

            match work:
                case "1":
                    work7__1_2()
                case "2":
                    work7__1_2()
                case "3":
                    work7__2()
                case _:
                    print("Нет такого варианта")
        case "8":
            ...
