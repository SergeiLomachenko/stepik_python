n = int(input())
matr = []
for i in range(n):
    stroka = [int(l) for l in input().split()]
    matr.append(stroka)
matr.reverse()
for f in range(len(matr)):
    for g in range(n):
        print(matr[g][f], end = ' ')
    print()
