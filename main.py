#Вариант 12 - вычислить определитель матрицы (3x3,2x2) 

def opredelitil_3x3(list1):
    return list1[0][0] * list1[1][1] * list1[2][2] + list1[0][1] * list1[1][2] * list1[2][0] + list1[0][2] * list1[1][0] * list1[2][1] - list1[2][0] * list1[1][1] * list1[0][2] - list1[2][1] * list1[1][2] * list1[0][0] - list1[2][2] * list1[1][0] * list1[0][1]
def opredelitil_2x2(list1):
    return list1[0][0] * list1[1][1] - list1[0][1] * list1[1][0]


