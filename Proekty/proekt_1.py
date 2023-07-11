from random import *
def is_valid():
    if (n.isdigit() == True) and ((int(n) >= 1) and (int(n) <= 100)):
        return True
    else:
        return False
rand = randint(1, 100)
count = 1
while True:
    n = input("Введите число: ")

    if is_valid() == True:
        n = int(n)
        if n < rand:
            print('Ваше число меньше загаданного, попробуйте еще разок')
            count += 1
        elif n > rand:
            print('Ваше число больше загаданного, попробуйте еще разок')
            count += 1
        else:
            print('Вы угадали, поздравляем!')
            break

print("Спасибо, что играли в числовую угадайку. Еще увидимся... Количество попыток : ", count)
