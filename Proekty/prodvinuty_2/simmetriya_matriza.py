n = int(input())
matr = []
for k in range(n):
    stroka = [int(l) for l in input().split()]
    matr.append(stroka)

for i in range(n):
    for j in range(n):
        a = True
        if matr[i][j] != matr[j][i]:
            a = False
            break

if a == True:
    print("YES")
else:
    print("NO")
