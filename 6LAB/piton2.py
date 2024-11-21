def is_latin(word):
    for char in word:
        if not ('a' <= char <= 'z' or 'A' <= char <= 'Z'):
            return False
    return True

def custom_append(lst, item):
    lst += [item]
    return lst

def split_text(text):
    words = []
    word = ''
    for char in text:
        if char == ' ':
            if word:
                words = custom_append(words, word)
                word = ''
        else:
            word += char
    if word: 
        words = custom_append(words, word)
    return words

def join_words(words, separator=' '):
    result = ''
    for i in range(len(words)):
        result += words[i]
        if i < (len(words)-1):
            result += separator
    return result

def custom_all(iterable):
    for element in iterable:
        if not element:
            return False
    return True

def filter_words(text):
    words = split_text(text)  
    if not custom_all(is_latin(word) for word in words): 
        return "Ошибка: Текст должен содержать только латинские буквы!"

    if len(words) < 2 or len(words) > 30:  
        return "Ошибка: В тексте должно быть от 2 до 30 слов."

    if not custom_all(2 <= len(word) <= 10 for word in words):
        return "Ошибка: Каждое слово должно содержать от 2 до 10 букв."

    last_word = words[-1]
    filtered_words = []

    for word in words[:-1]: 
        if word != last_word:
            filtered_words = custom_append(filtered_words, word) 

    return join_words(filtered_words)

text = str(input("Введите текст на латинице: "))
result = filter_words(text)
print("Текст со всеми словами, отличынми от последнего: ",result)