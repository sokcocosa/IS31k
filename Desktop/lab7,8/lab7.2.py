
def stroka():
    b = input("Строка для вхождения: ")
    a = input("Строка для проверки: ")


    count = 0
    ab = ""
    for i in b:
        if i in a:
            ab = ab + i
        else:
            ab = ""
        if a in ab:
            count += 1
            if ab[0] == ab[-1]:
                ab = ab[-1]
            else:
                ab = ""
    return count
print(stroka())

input()