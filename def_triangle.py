# объявление функции
def is_valid_triangle(s1, s2, s3):
    if s1 + s2 > s3 and s1 + s3 > s2 and s2 + s3 > s1 :
        print('True')
    else:
        print('False')
# считываем данные
a, b, c = int(input()), int(input()), int(input())

# вызываем функцию
is_valid_triangle(a, b, c)