n = int(input())
m = int(input())
matr = []
for k in range(n):
    stroka = [int(l) for l in input().split()]
    matr.append(stroka)
i, j = [int(h) for h in input().split()]
for t in range(len(matr)):
    matr[t][i], matr[t][j] = matr[t][j], matr[t][i]
for f in range(len(matr)):
    for g in range(m):
        print(matr[f][g], end = ' ')
    print()