import matrix

if __name__ == "__main__":
    w = int(input("Введите длину матрицы: "))
    h = int(input("Введите ширину матрицы: "))

    matrx = matrix.create_matrix(h, w)
    
    print(matrx) # вывод самой матрицы

    print(matrix.maximum_element(matrx)) # вывод максимального элемента матрицы
