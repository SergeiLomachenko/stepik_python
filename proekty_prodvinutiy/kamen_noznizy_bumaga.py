print("Добро пожаловать в игру 'Камень, ножницы, бумага'!")
sp = ["камень", "ножницы", "бумага"]
def an(s1, s2):
    if s1 == s2:
        print("Итог игры: ничья")
    elif s1 == "ножницы" and s2 == "бумага":
        print("Победил, Игрок 1")
    elif s1 == "камень" and s2 == "ножницы":
        print("Победил, Игрок 1")
    elif s1 == "бумага" and s2 == "камень":
        print("Победил, Игрок 1")
    else:
        print("Победил, Игрок 2")

def bn():
    global slovo1
    global slovo2
    print("Игрок 1, введите ваше слово")
    slovo1 = input()
    while slovo1 not in sp:
        print("Игрок 1, пожалуйста, введите корректное слово!")
        slovo1 = input()

    print("Игрок 2, введите ваше слово")
    slovo2 = input()
    while slovo2 not in sp:
        print("Игрок 2, пожалуйста, введите корректное слово!")
        slovo2 = input()
bn()
an(slovo1, slovo2)

def cn():
    print("Хотите сыграть еще раз? Введите 'да/нет'")
    a = input()
    sp1 = ["да", "нет"]
    while a not in sp1:
        print("Пожалуйста, ответьте корректно 'да' или 'нет'")
    if a == 'да':
        bn()
        an(slovo1, slovo2)
    else:
        print("Спасибо за игру! До новых встреч!")
while True:
    cn()