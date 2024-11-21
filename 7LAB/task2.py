import random

print("Программа по формированию списка C размером N x 2N из списков A и B размером N x N: ")

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

N = valid("Введите размер матрицы N: ")

A = [[random.randint(0,9) for _ in range(N)] for _ in range(N)]
B = [[random.randint(0,9) for _ in range(N)] for _ in range(N)]

print("\nСписок A: ")
for row in A:
    print(row)

print("\nСписок B: ")
for row in B:
    print(row)

C = []
for i in range(N):
    row = A[i] + B[i]
    C.append(row)

print("\nСписок С: ")
for row in C:
    print(row)
