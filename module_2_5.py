def get_matrix(n, m, value):
    matrix = []
    for i in range(n):
        matrix.append([])
        for j in range(m):
            matrix[i].append(value)
    print(matrix)
    return matrix

n = int(input(f'Введите число строк матрицы: '))
m = int(input(f'Введите число столбцов матрицы: '))
value = input(f'Введите значения матрицы: ')
print('--------------' * m)
matrix = get_matrix(n, m, value)

if n <= 0:
    print(f"Вы не ввели число строк:", n)
elif m <= 0:
    print(f"Вы не ввели число столбцов:", m)
else:
    print(f"Матрица построина:")
    for i in matrix:
        print(*i)