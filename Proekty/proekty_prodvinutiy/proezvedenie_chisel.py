k = int(input())
spisok1 = []
for m in range(k):
    a = int(input())
    spisok1.append(a)
spisok2 = []
for i in range(k):
    for j in range(i):
        b = spisok1[i] * spisok1[j]
        spisok2.append(b)

chislo = int(input())
count = 0
if chislo in spisok2 and spisok1[i] is not spisok1[j]:
    count += 1
if count >= 1:
    print("ДА")
else:
    print("НЕТ")