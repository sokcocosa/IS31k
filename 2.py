ss = input()
s = input()

n = 0
i = 1

while i != -1:
    i = ss.find(s)
    if i >= 0:
        n += 1
    ss = ss[i + 1:]
print(n)