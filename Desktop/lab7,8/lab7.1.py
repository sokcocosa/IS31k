
def urav():
    try:
        a = int(input("Введите A: "))
        b = int(input("Введите B: "))
        c = int(input("Введите C: "))
    except ValueError:
        print("Нужны числа!")
        return
    if a == 0 and b != 0 and c != 0:
        print("Неквадратное уравнение")
        return
    elif a == 0 and b == 0 or a == 0 and c == 0:
        print("Неразрешимое уравнение")
        return
    D = b**2 - 4 * a * c

    if D < 0:
        print("Случай комплексных корней")
    elif D > 0:
        print("Уравнение имеет два корня\nx1 = ", (-b - D ** 0.5) / (2 * a))
        print("x2 = ", (-b + D**0.5)/(2 * a))
    elif D == 0:
        print("Уравнение имеет один корень x = ", -b/(2 * a))

urav()

input()