def draw_triangle():
    for i in range(9):
        print(' ' * (8 - i) + '*' * (i + (i -1)), sep = '')

# основная программа
draw_triangle()  # вызов функции