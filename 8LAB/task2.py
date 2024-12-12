import math

def valid(zn):
    while True:
        try:
            value = float(input(zn))
            return value
        except ValueError:
            print("Введите действительное число")

def func(a,b):
    return math.sqrt((a**2)+(b**2)+(math.sin(a*b)**2))

x = valid("Введите действительное число x: ")
y = valid("Введите действительное число y: ")
z = valid("Введите действительное число z: ")

S = func(x,y) + func(x,z) + func(y,z)
print("S =",S)