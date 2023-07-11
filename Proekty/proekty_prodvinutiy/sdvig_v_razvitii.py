n = input().split()
for i in range(len(n), 1, -1):
    n[i - 1], n[i - 2]  = n[i - 2], n[i - 1]
for j in range(len(n)):
    print(n[j], end = ' ')