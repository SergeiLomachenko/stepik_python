n = int(input())
matrix = []
for g in range(n):
    matrix1 = [int(l) for l in input().split()]
    matrix.append(matrix1)
sum = 0
for k in range(n):
    sum += matrix[k][k]
print(sum)