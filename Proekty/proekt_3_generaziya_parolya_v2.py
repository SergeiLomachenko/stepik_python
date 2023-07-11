import random

#константы
digits = '0123456789';
lowercase_letters = 'abcdefghijklmnopqrstuvwxyz';
uppercase_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ';
punctuation = '!#$%&*+-=?@^_';

#переменная
chars = ''

#переменные
q1 = input('Укажите количество паролей для генерации: ')
q2 = input('Укажите длину одного пароля: ')
q3 = input('Включать ли цифры 0123456789? (yes/no) ')
q4 = input('Включать ли прописные буквы ABCDEFGHIJKLMNOPQRSTUVWXYZ? (yes/no) ')
q5 = input('Включать ли строчные буквы abcdefghijklmnopqrstuvwxyz? (yes/no) ')
q6 = input('Включать ли символы !#$%&*+-=?@^_? (yes/no) ')
q7 = input('Исключать ли неоднозначные символы il1Lo0O? (yes/no) ')

#генерация пароля
if q3 == 'yes':
    chars = chars + digits
if q4 == 'yes':
    chars = chars + lowercase_letters
if q5 == 'yes':
    chars = chars + uppercase_letters
if q6 == 'yes':
    chars = chars + punctuation
for i in range(int(q1)):
    if q7 == 'yes':
        for c in 'il1Lo0O':
            chars = chars.replace(c,'')
    print(*random.sample(chars, int(q2)), sep='')
