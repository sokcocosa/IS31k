from random import randint
n = 3 #int(input('размер матрицы:\n'))
a = []
asum = 0
for i in range(n):
    a.append([])
    for j in range(n):
        a[i].append(randint(-99, 99))
        if i < j:
            asum += a[i][j]
    print(*map(format, a[i]))
print(asum)
