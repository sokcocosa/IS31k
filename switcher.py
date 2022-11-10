import os

if __name__ == "__main__":
    choice = int(input("Введите вариант работы(1-18): "))

    lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18]

    if choice in lst:
        if os.system(f"git switch {choice}") == 0:
            print(f"\033[33mИдет выполнение работы\033[0m \033[31m{choice}\033[33m варианта\033[0m")
            os.system("python main.py")
        else:
            print("\033[31mОшибка!\033[0m\nВетка не была найдена. Попробуйте обновить командой \033[33mgit pull\033[0m")
    else:
        print("\033[31mОшибка!\033[0m\nДоступные значение с 1 до 18")
