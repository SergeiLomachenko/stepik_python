# объявление функции
def is_prime(num):
    delitel = 0
    Flag = True
    for i in range(1, num + 1):
        if num % i == 0:
            delitel += 1
    if delitel > 2:
        Flag = False
    if num < 2:
        Flag = False
    print(Flag)

# считываем данные
n = int(input())
# вызываем функцию
is_prime(n)