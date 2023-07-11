import math
n= int(input())
matrix = []
for k in range(n):
    stroka = [int(l) for l in input().split()]
    matrix.append(stroka)
spisok = []
for i in range(n):
    for j in range(n):
        if i >= j and i <= (n - 1 - j):
            spisok.append(matrix[i][j])
        if i < j and i >= (n - 1 - j):
            spisok.append(matrix[i][j])
        if i == j and i <= math.ceil(n / 2):
            spisok.append(matrix[i][j])
print(max(spisok))