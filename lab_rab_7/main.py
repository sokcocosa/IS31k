# Задание №1
'''import math

print("Введите коэффициенты для уравнения")
print("ax^2 + bx + c = 0:")
a = float(input("a = "))
b = float(input("b = "))
c = float(input("c = "))

discr = b ** 2 - 4 * a * c
if a == 0 and b == 0:
    print("Неразрешимое уравнение")
elif a == 0:
    print("Неквадратное уравнение")
elif discr < 0:
    print("Случай комплексных чисел")
elif b == 0 and c == 0:
    print("x1 = x2 = 0")
else:
    print("Дискриминант D = %.2f" % discr)
    if discr > 0:
        x1 = (-b + math.sqrt(discr)) / (2 * a)
        x2 = (-b - math.sqrt(discr)) / (2 * a)
        print("x1 = %.2f \nx2 = %.2f" % (x1, x2))
    elif discr == 0:
        x = -b / (2 * a)
        print("x = %.2f" % x)'''

# Задание №2

'''str1 = input("Строка 1: ")
str2 = input("Строка 2: ")
count = 0
ind = 1
while ind != -1:
    ind = str1.find(str2)
    if ind >= 0:
        count += 1
    str1 = str1[ind+1:]
print("Вывод: " + str(count))'''


# Задание №1 8 лаб.раб.
'''
dict = {'A': 11, 'B': 12, 'C': 13, 'D':14, 'E': 15,
        'F': 21, 'G': 22, 'H': 23, 'I': 24, 'J': 24, 'K': 25,
        'L': 31, 'M': 32, 'N': 33, 'O':34, 'P':35,
        'Q': 41, 'R': 42, 'S': 43, 'T': 44, 'U': 45,
        'V': 51, 'W': 52, 'X': 53, 'Y': 54, 'Z': 55
}


def encode(sentence):
        new_frase = ''
        lst_frase = list(sentence)
        for i in sentence:
                if i in dict:
                        new_frase += str(dict.get(i))
                else:
                        new_frase += (i + i)
        if sentence.isnumeric():
                return f'Введите буквы!'
        return new_frase


def decode(sentence):
        try:
                new_frase = ''
                lst_frase = []

                step = 2
                for i in range(0, len(sentence), 2):
                        lst_frase.append(sentence[i:step])
                        step += 2

                k = list(dict.keys())
                v = list(dict.values())

                lst_frase = list(map(int, lst_frase))
                for i in lst_frase:
                        if i in v:
                                x = v.index(i)
                                new_frase += k[x]
                        else:
                                new_frase += i[0:1]

                return new_frase
        except (ValueError, TypeError) as e:
                return 'Введите корректные значения!'


print(encode(input('Введите слово для зашифровки: ').upper()))
print(decode(input('Введите число для расшифровки: ')))
'''