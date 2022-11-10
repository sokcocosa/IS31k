import random
Variant2=int(input("Матрица: "))
ggg=[[random.randint(1,9) for i in range(Variant2)] for j in range(Variant2)]
min = ggg[0][0]
for i in range(Variant2):
    for j in range(Variant2):
        if(ggg[i][j]<min): min=ggg[i][j]
for i in range(Variant2): print(ggg[i])
print(min)