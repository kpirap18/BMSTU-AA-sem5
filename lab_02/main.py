def print_matrix(matrix):
   for i in range (len(matrix)):
      print(matrix[i])


def read_matrix():
    row_num = int(input("Введите количество строк: "))
    column_num = int(input("Введите количество столбцов: "))
    m = []
    for i in range(row_num):
        arr = list(int(i) for i in input("Введите строку: ").split())
        if (len(arr) != column_num):
            print("Не все столбцы заполнены! Ошибка!")
            i -= 1
        else:
            m.append(arr)
    return m


def simple_matrix_mult(matrix1, matrix2):
    if (len(matrix1[0]) != len(matrix2)):
        print("Error size matrix!")
        return -1

    n = len(matrix1)
    m = len(matrix1[0])
    q = len(matrix2[0])

    matrix_res = [[0] * q for i in range(n)]

    for i in range(n):
        for j in range(q):
            for k in range(m):
                matrix_res[i][j] = matrix_res[i][j] +\
                                   matrix1[i][k] * matrix2[k][j]

    return matrix_res


def winograd_matrix_mult(matrix1, matrix2):
    if (len(matrix1[0]) != len(matrix2)):
        print("Error size matrix!")
        return -1

    n = len(matrix1)
    m = len(matrix1[0])
    q = len(matrix2[0])

    matrix_res = [[0] * q for i in range(n)]

    row_factor = [0] * n
    for i in range(n):
        for j in range(0, m // 2, 1):
            row_factor[i] = row_factor[i] + \
                            matrix1[i][2 * j] * matrix1[i][2 * j + 1]

    column_factor = [0] * q
    for i in range(q):
        for j in range(0, m // 2, 1):
            column_factor[i] = column_factor[i] + \
                               matrix2[2 * j][i] * matrix2[2 * j + 1][i]

    for i in range(n):
        for j in range(q):
            matrix_res[i][j] = -row_factor[i] - column_factor[j]
            for k in range(0, m // 2, 1):
                matrix_res[i][j] = matrix_res[i][j] +\
                        (matrix1[i][2 * k + 1] + matrix2[2 * k][j]) * \
                        (matrix1[i][2 * k] + matrix2[2 * k + 1][j])

    if m % 2 == 1:
        for i in range(n):
            for j in range(q):
                matrix_res[i][j] = matrix_res[i][j] +\
                                   matrix1[i][m - 1] * matrix2[m - 1][j]

    return matrix_res


def winograd_matrix_mult_opim(matrix1, matrix2):
    if (len(matrix1[0]) != len(matrix2)):
        print("Error size matrix!")
        return -1

    n = len(matrix1)
    m = len(matrix1[0])
    q = len(matrix2[0])

    matrix_res = [[0] * q for i in range(n)]

    row_factor = [0] * n
    for i in range(n):
        for j in range(1, m, 2):
            row_factor[i] += matrix1[i][j] * matrix1[i][j - 1]

    column_factor = [0] * q
    for i in range(q):
        for j in range(1, m, 2):
            column_factor[i] += matrix2[j][i] * matrix2[j - 1][i]

    flag = m % 2
    for i in range(n):
        for j in range(q):
            matrix_res[i][j] = -(row_factor[i] + column_factor[j])
            for k in range(1, m, 2):
                matrix_res[i][j] += (matrix1[i][k - 1] + matrix2[k][j]) * \
                                    (matrix1[i][k] + matrix2[k - 1][j])
            if (flag):
                matrix_res[i][j] += matrix1[i][m - 1] \
                                    * matrix2[m - 1][j]

    return matrix_res


if __name__ == "__main__":
    print("Введите матрицу 1: ")
    m1 = read_matrix()

    print("Введите матрицу 2: ")
    m2 = read_matrix()

    print("Результат, посчитанный классическим алгоритмом: ")
    m_base = simple_matrix_mult(m1, m2)
    print_matrix(m_base)

    print("Результат, посчитанный алгоритмом Винограда: ")
    m_vin = winograd_matrix_mult(m1, m2)
    print_matrix(m_vin)

    print("Результат, посчитанный оптимизированным алгоритмом Винограда: ")
    m_opt_vin = winograd_matrix_mult_opim(m1, m2)
    print_matrix(m_opt_vin)