def find(substring, string, start=0):
    length = len(substring)  # Длина подстроки
    for i in range(start, len(string)):  # Проход по всем возможным позициям для подстроки
        if string[i:i+length] == substring:  # Сравнение части строки с подстрокой
            return i  
    return -1  

def count_substring(s, s0):
    count = 0  
    start_index = 0  
    while True:
        index = find(s0, s, start_index)  # Поиск подстроки, начиная с текущей позиции
        if index == -1:  
            break  
        count += 1  
        start_index = index + len(s0) # Сдвигаемся вперед 
    return count

print("Программа по нахождению числа количества вхождений строки S0 в строку S")
s = str(input("Введите строку S: "))
s0 = str(input("Введите строку S0: "))
print(f"Количество вхождений строки S0 в строку S = {count_substring(s, s0)}")

