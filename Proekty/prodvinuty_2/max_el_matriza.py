n = int(input())
m = int(input())
matr = []
for j in range(n):
    mult = [int(i) for i in input().split()]
    matr.append(mult)
maksim = []
for k in range(len(matr)):
    maksim.append(max(matr[k]))
max_el = max(maksim)
a1 = maksim.index(max_el)
a2 = matr[a1].index(max_el)

print(a1, a2)
