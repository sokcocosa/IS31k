import random
Variant3=int(input("Матрица: "))
ggg=[[random.randint(1,9) for i in range(Variant3)] for j in range(Variant3)]
min = ggg[0][0]
for i in range(Variant3):
    for j in range(Variant3):
        if(ggg[i][j]<min): min=ggg[i][j]
for i in range(Variant3): print(ggg[i])
print(min)
