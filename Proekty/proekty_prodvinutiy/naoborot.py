n = input().split()
k = []
for i in range(0, len(n) - 1, 2):
    x = n[i]
    y = n[i+1]
    x, y = y, x
    k.append(x)
    k.append(y)
if (len(n) % 2) == 1:
    k.append(n[-1])
for j in range(len(k) - 1):
    print(k[j], end = ' ')
print(k[-1], end ='')