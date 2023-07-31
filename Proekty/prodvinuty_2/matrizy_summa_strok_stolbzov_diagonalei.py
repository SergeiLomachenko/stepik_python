n = int(input())
matr = []
for i in range(n):
    m = [int(l) for l in input().split()]
    matr.append(m)
diapazon = [int(f) for f in range(1, n ** 2 + 1)]

summa_strok_stolbzov_diagonalei = []
for j in range(len(matr)):
    s1 = 0
    for k in range(len(matr)):
        s1 = s1 + matr[j][k]
    summa_strok_stolbzov_diagonalei.append(s1)

for j in range(len(matr)):
    s2 = 0
    for k in range(len(matr)):
        s2 = s2 + matr[k][j]
    summa_strok_stolbzov_diagonalei.append(s2)

s3 = 0
s4 = 0
for k in range(len(matr)):
    s3 = s3 + matr[k][n - k - 1]
    s4 = s4 + matr[n - k - 1][k]
summa_strok_stolbzov_diagonalei.append(s3)
summa_strok_stolbzov_diagonalei.append(s4)

chisla_matrizy = []
for c in range(len(matr)):
    for t in range(len(matr)):
        chisla_matrizy.append(int(matr[c][t]))

Flag = True
for s in range(len(chisla_matrizy)):
    if diapazon[s] not in chisla_matrizy:
        Flag = False

for x in range(1, len(summa_strok_stolbzov_diagonalei)):
    if summa_strok_stolbzov_diagonalei[x] != summa_strok_stolbzov_diagonalei[x - 1]:
        Flag = False
if Flag == True:
    print("YES")
else:
    print("NO")
