def isInt (zn):
    while True:
        try:
            value = int(input(zn))
            return value
        except ValueError:
            print("Введите целое число")

def isReal(zn):
    while True:
        try:
            value = float(input(zn))
            return value
        except ValueError:
            print("Введите вещественное число")

def PowerN(X,N):
    if N == 0:
        return 1
    
    if N >0:
        if N % 2 ==0:
            return (PowerN(X,N//2)**2)
        if N % 2 ==1:
            return X* PowerN(X,N-1)
        
    if N < 0:
        return 1/PowerN(X,-N)

X = isReal("Введите число X: ")
N = [isInt(f"Введите значение N{i+1}: ") for i in range(5)]

for N in N:
    print(f"X^{N} = {PowerN(X,N)}")