n = input().split()
res = [[n[0]]]
for i in range(1, len(n)):
    if n[i] == n[i - 1]:
        res[-1].append(n[i])
    else:
        res.append([n[i]])
print(res)