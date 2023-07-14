n = int(input())
matr = []
for i in range(n):
    stroka = [int(l) for l in input().split()]
    matr.append(stroka)
for j in range(n // 2):
    for k in range(n):
        matr[j][k], matr[n-j-1][k] = matr[n-j-1][k], matr[j][k]
for f in range(len(matr)):
    for g in range(n):
        print(matr[f][g], end = ' ')
    print()
