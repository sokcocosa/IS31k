import random
Variant4=int(input("Матрица: "))
ggg=[[random.randint(1,9) for i in range(Variant4)] for j in range(Variant4)]
min = ggg[0][0]
for i in range(Variant4):
    for j in range(Variant4):
        if(ggg[i][j]<min): min=ggg[i][j]
for i in range(Variant4): print(ggg[i])
max = ggg[0][0]
for i in range(Variant4):
    for j in range(Variant4):
        if(ggg[i][j]>max): max=ggg[i][j]
print(min)
print(max)
print(max - min)