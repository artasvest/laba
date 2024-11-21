while True:
    stroka = input("Введите строку: ").strip()
    stroka = stroka.replace(" ", "")
    if not stroka.isalpha():
        print("Строка должна содержать только буквы. Введите её ещё раз.")
    else:
        break
    
print("\nИсходная строка: ", stroka)

lettersin = {}
for letter in stroka:
    if letter.isalpha():
        if letter in lettersin:
            lettersin[letter] +=1
        else:
            lettersin[letter] = 1

print("\nСловарь букв и их количества:")
for key,value in lettersin.items():
    print(f"'{key}': {value}")