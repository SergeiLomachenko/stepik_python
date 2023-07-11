#оглавление
import random
print('Добро пожаловать в числовую угадайку')

#ниже функция с проверкой на значение для левой границы
def is_valid(num):

    if num.isdigit() != True:
        return False

    if int(num) not in range(1, int(right)+1):
        return False

    return True

#ниже функция с проверкой на значение
def is_valid_right(num):

    if num.isdigit() != True:
        return False

    if int(num) < 2:
        return False

    return True

#ниже тело функции
def lets_guess():
    global right

    right = input('Сейчас я загадаю число от одного до... до скольки? \n')

    while is_valid_right(right) != True:
        right = input('Меня не обманешь. Введи число от двух и больше \n')

    answer = random.randint(1, int(right))
    counter = 1

    while True:
        num = input('Это попытка №' + str(counter) + '. Введи число от 1 до ' + right + '. \n')

        while is_valid(num) != True:
            num = input('А может быть все-таки введем целое число от 1 до ' + right + '? \n')

        num = int(num)
        counter += 1

        if num < answer:
            print('Это число меньше загаданного, попробуй еще разок')

        if num > answer:
            print('Это число больше загаданного, попробуй еще разок')

        if num == answer:
            again = input('Ты угадал, поздравляем! Хочешь попробовать ещё? Напиши "Да" либо "Нет". \n')

            while again.lower() != 'да' and again.lower() != 'нет':
                again = input('Ничего не понимаю. Введи "Да" или "Нет"! \n')

            if again.lower() == 'да':
                lets_guess()

            elif again.lower() == 'нет':
                print('Спасибо, что сыграл в числовую угадайку. Еще увидимся...')

            break


lets_guess()
