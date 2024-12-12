import random

def matrixSum(matrix1,matrix2):
    resmat = [[0 for _ in range(N)] for _ in range(M)]
    for row in range(M):
        for col in range(N):
            resmat[row][col] = matrix1[row][col]+matrix2[row][col]
    return resmat

def matrixSubs(matrix1,matrix2):
    resmat = [[0 for _ in range(N)] for _ in range(M)]
    for row in range(M):
        for col in range(N):
            resmat[row][col] = matrix1[row][col]-matrix2[row][col]
    return resmat

def valid(zn):
    while True:
        try:
            value = int(input(zn))
            if value > 0:
                return value
            else:
                print("Число должно быть положительным")
        except ValueError:
            print("Введите целое число")

M = valid("Введите количество строк M: ")
N = valid("Введите количество столбцов N: ")

matrixA = [[random.randint(0,9) for _ in range(N)] for _ in range(M)]
matrixB = [[random.randint(0,9) for _ in range(N)] for _ in range(M)]
matrixC = [[random.randint(0,9) for _ in range(N)] for _ in range(M)]
matrixD = [[random.randint(0,9) for _ in range(N)] for _ in range(M)]
matrixP = [[0 for _ in range(N)] for _ in range(M)]

print("\nИсходные матрицы:")

print("\nМатрица A:")
for row in matrixA:
    print(row)

print("\nМатрица B:")
for row in matrixB:
    print(row)

print("\nМатрица C:")
for row in matrixC:
    print(row)

print("\nМатрица D:")
for row in matrixD:
    print(row)

matrixP = matrixSubs(matrixSum(matrixA,matrixB),matrixSum(matrixC,matrixD))

print("\nМатрица P:")
for row in matrixP:
    print(row)
