n = input().split()
count = 1
for i in range(1, len(n)):
    if int(n[i]) > int(n[i - 1]):
        count += 1
print(count)