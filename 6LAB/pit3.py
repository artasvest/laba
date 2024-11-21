def int_input():
    while True:
        try:
            n = int(input("Введите длину списка: "))
            return n
        except ValueError:
            print("Ошибка: длина списка должна быть целым числом")

import random

n = int_input()
min_value = -100
max_value = 100

minus1 = 0
minus2= 0

summamin = 0
summanech = 0

spisok = [random.randint(min_value,max_value) for _ in range(n)]

for i in range(len(spisok)):
    if spisok[i]<0:
        minus1 = i
        break

for i in range(minus1,len(spisok)):
    if spisok[i]<0:
        minus2= i

for i in range(minus1+1,minus2):
    summamin += spisok[i]

for i in range(len(spisok)):
    if i%2!=0:
        summanech += spisok[i]

print("Сам список: ",spisok)
print("Сумма элементов списка с нечетными номерами равна: ",summanech)
print("Сумма элементов списка, расположенных между первым и последним отрицательными элементами равна: ",summamin)

