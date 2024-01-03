n = int(input())

matr = []
for i in range(n):
    mi = []
    for j in range(n):
        if i == n - j - 1 or i == j:
            mi.append('1 ')
        else:
            mi.append('0 ')
    matr.append(mi)
for t in range(len(matr)):
    for r in range(len(matr)):
        print(str(matr[t][r]).ljust(3), end = '')
    print()
