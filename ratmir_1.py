from random import randint

n = 4
a = []
sum = 0

for i in range(n):
    a.append([])
    for j in range(n):
        a[i].append(randint(-1000, 1000))
        if i < j:
            sum += a[i][j]
    print(*map('{:>3}'.format, a[i]))

print(sum)