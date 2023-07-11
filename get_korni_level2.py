def solve(a, b, c):
    import math
    d = (b**2) - (4 * a * c)
    if d == 0 :
        x1 = -b / (2 * a)
        return x1, x1
    if d > 0 :
        x1 = (-b - math.sqrt(d)) / (2 * a)
        x2 = (-b + math.sqrt(d)) / (2 * a)
        if x1 <= x2:
            return x1, x2
        if x1 > x2:
            return x2, x1
# считываем данные
a, b, c = int(input()), int(input()), int(input())

# вызываем функцию
x1, x2 = solve(a, b, c)
print(x1, x2)