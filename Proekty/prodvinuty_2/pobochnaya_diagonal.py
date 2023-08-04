n = int(input())

matr = []
for i in range(n):
    mi = []
    for j in range(n):

        if (i + j + 1) == n:
            mi.append('1 ')
        if (i + j + 1) > n:
            mi.append('2 ')
        if (i + j + 1) < n:
            mi.append('0 ')
    matr.append(mi)
for t in range(len(matr)):
    for r in range(len(matr)):
        print(matr[t][r], end='')
    print()