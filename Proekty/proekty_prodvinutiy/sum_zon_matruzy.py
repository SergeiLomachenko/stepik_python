import math

n = int(input())
matrix = []
for k in range(n):
    stroka = [int(l) for l in input().split()]
    matrix.append(stroka)
spisok1 = []
spisok2 = []
spisok3 = []
spisok4 = []
for i in range(n):
    for j in range(n):

        if i < j and i < (n - 1 - j):
            spisok1.append(matrix[i][j])
        if i < j and i > (n - 1 - j):
            spisok2.append(matrix[i][j])
        if i > j and i > (n - 1 - j):
            spisok3.append(matrix[i][j])
        if i > j and i < (n - 1 - j):
            spisok4.append(matrix[i][j])

print(f'''
Верхняя четверть: {sum(spisok1)}
Правая четверть: {sum(spisok2)}
Нижняя четверть: {sum(spisok3)}
Левая четверть: {sum(spisok4)} 
''')
