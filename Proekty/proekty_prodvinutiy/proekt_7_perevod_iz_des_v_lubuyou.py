print('Вас приветствует калькулятор переводчик из десятичную сс в какую-то случайную сс.')
def f4():
    print('Введите число')
    number = int(input())
def f1(num):
    count, result = len(num)-1, 0
    hexdict = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 'A', 'B', 'C', 'D', 'E', 'F']
    for i in num:
        for j in range(len(hexdict)):
            if i == str(hexdict[j]):
                result += j * 16 ** count
                count -= 1
    return result

def f2(num):
    hexdict, rez = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 'A', 'B', 'C', 'D', 'E', 'F'], ''
    while num != 0:
        a = num % 16
        b = num // 16
        rez += str(hexdict[a])
        num = b
    return rez[::-1]


def f3(num):
    count, result = len(num)-1, 0
    for i in num:
        result += int(i) * 8 ** count
        count -= 1
    return result

    a1 = f1(number)
    a2 = f2(number)
    a3 = f3(number)

while True:
    f4()
    a1 = f1(number)
    a2 = f2(number)
    a3 = f3(number)
    print('Результат в шеснадцатиричной сс =', a1)
    print('Результат в восьмиричной сс =', a3)
    output = input('Если желаете покинуть программу, просто напишите EXIT и нажмите ENTER\nВ противном случае нажмите ENTER\n')
    if output == 'EXIT':
        break

