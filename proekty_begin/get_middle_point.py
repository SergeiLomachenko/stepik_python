def get_middle_point(x1, y1, x2, y2):
    k1 = (x1 + x2) / 2
    k2 = (y1 + y2) / 2
    return k1, k2
# считываем данные
x_1, y_1 = int(input()), int(input())
x_2, y_2 = int(input()), int(input())

# вызываем функцию
k1, k2 = get_middle_point(x_1, y_1, x_2, y_2)
print(k1, k2)