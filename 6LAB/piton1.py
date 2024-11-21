def find(substring, string, start=0):
    length = len(substring)
    for i in range(start, len(string)):
        if string[i:i+length] == substring: 
            return i  
    return -1  

def count_substring(s, s0):
    count = 0  
    start_index = 0
    while True:
        index = find(s0, s, start_index) 
        if index == -1:
            break
        count += 1
        start_index = index + len(s0)
    return count

print("Программа по нахождению числа количества вхождений строки S0 в строку S")
s = str(input("Введите строку S: "))
s0 = str(input("Введите строку S0: "))
print(f"Количество вхождений строки S0 в строку S = {count_substring(s, s0)}")

