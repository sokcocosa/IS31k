import random

X = [[random.randint(0, 10),random.randint(0, 10),random.randint(0, 10)],
     [random.randint(0, 10),random.randint(0, 10),random.randint(0, 10)],
     [random.randint(0, 10),random.randint(0, 10),random.randint(0, 10)]]

Y = [[random.randint(0, 10),random.randint(0, 10),random.randint(0, 10)],
     [random.randint(0, 10),random.randint(0, 10),random.randint(0, 10)],
     [random.randint(0, 10),random.randint(0, 10),random.randint(0, 10)]]

result = [[0,0,0],[0,0,0],[0,0,0]]

for i in range(len(X)):
   for j in range(len(X[0])):
        result[i][j] = X[i][j] + Y[i][j]
print("Матрица X:")
for X1 in X:
      print(X1)
print("==================================")
print("Матрица Y:")
for Y1 in Y:
      print(Y1)
print("==================================")
print("Сумма матриц X и Y:")
for r in result:
      print(r)