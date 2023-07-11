import random
def is_valid(num):
    if num.isdigit() and 1 <= int(num) <= 100:
        return True
    else:
        return False

num = input("Введи строку:")
print(is_valid(num))