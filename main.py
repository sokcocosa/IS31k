from math import *

print("Введите исходные данные: ")
print("a = ", end='')
a = float(input())
print("b = ", end='')
b = float(input())
print("eps = ", end='')
e = float(input())
print("Вы ввели: ")
print("a = %.2f  b = %.2f  eps = %.2e" % (a, b, e))

y = log(a) - a + 1.8

while b-a >= e:
    x = (a+b)/2
    z = log(x) - x + 1.8
    if y*z < 0:
            b = x
    else:
        a = x
        y = z

print("x =", x, "z =",z)



