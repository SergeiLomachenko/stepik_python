# объявление функции
def func(num1, num2):
    return num1 % num2 == 0

# считываем данные
n1, n2 = int(input()), int(input())

func(n1, n2)
if func(n1, n2):
    print("делится")
else:
    print("не делится")