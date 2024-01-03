def is_pangram(text):
    stroka = "abcdefghijklmnopqrstuvwxyz"
    Flag = True
    for i in range(len(stroka)):
        if stroka[i] not in text.lower():
            Flag = False
    return Flag

# считываем данные
text = input()

# вызываем функцию
print(is_pangram(text))