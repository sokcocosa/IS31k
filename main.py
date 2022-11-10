from random import randint
n = int(input("Введите длину динамического массива : "))
a = [[randint(0,100)
     for i in range(n)]]
b = [[randint(0,100)
     for i in range(n)]]  
s = 0
r = 0
for i in range(len(a)):
    for j in range(len(a[i])):
        s += a[i][j]
for i in range(len(b)):
    for j in range(len(b[i])):
        s +=b[i][j]
print(s)
for i in range(len(a)):
    for j in range(len(a[i])):
        r-= a[i][j]
for i in range(len(b)):
    for j in range(len(b[i])):
        r -=b[i][j]
print(r)