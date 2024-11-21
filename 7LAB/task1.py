import random

print("Программа по нахождению количества столбцов в списке M x N, не содержащих ни одного нулевого элемента")

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

matrix = [[random.randint(0,9) for _ in range(N)] for _ in range(M)]


print("\nИсходная матрица:")

for row in matrix:
    print(row)

count = 0
for col in range(N):
    for row in range(M):
        if matrix[row][col] == 0:
            break
    else:
        count +=1


print("\nКоличество столбцов в списке, не содержащих ни одного нулевого элемента: ", count)