n = int(input())
m = int(input())
a = [[0]*m for _ in range(n)]
for i in range(n):
    for j in range(m):
        a[i][j] = input()
    print(*a[i])
print()
for j in range(m):
    for i in range(n):
        print(a[i][j], end = ' ')
    print()