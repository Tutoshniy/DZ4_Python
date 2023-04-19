# Напишите функцию для транспонирования матрицы .

matrix = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]


def trans_matrix(data):
    copy_matrix = []
    for i in range(len(data)):
        copy_matrix.append([])
        for j in range(len(data[i])):
            copy_matrix[i].append(data[j][i])
    return copy_matrix


print(trans_matrix(matrix))
