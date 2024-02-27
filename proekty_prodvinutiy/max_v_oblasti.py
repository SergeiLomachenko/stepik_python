n = int(input())
matrix = []
for i in range(n):
    elem = [int(j) for j in input().split()]
    matrix.append(elem)
spisok = []
for k in range(n):
    for l in range(n):
        if k >= l and k >= (n - 1 - l):
            spisok.append(matrix[k][l])
        if k >= l and k <= (n - 1 - l):
            spisok.append(matrix[k][l])
        if k == l:
            spisok.append(matrix[k][l])
max_elem = max(spisok)
print(max_elem)