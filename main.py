from FirstRandom import CustomRandom as FirstPositive
from SecondRandom import CustomRandom as SecondNegative

if __name__ == "__main__":
    print("1. Случайное целое положительное число от 0 до 100")
    print("2. Случайное целое отрицательное число от 0 до 100")
    v = input("Введите вариант генерации случайного числа: ")
    match v.split():
        case ['1']:
            print(FirstPositive.positiveRandom())
        case ['2']:
            print(SecondNegative.negativeRandom())
        case _:
            print("Нет такого функционала")
