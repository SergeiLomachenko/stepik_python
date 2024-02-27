stroka = input().split()
count = 0
for i in range(1, len(stroka)):
    if int(stroka[i]) > int(stroka[i - 1]):
        count += 1
print(count)
