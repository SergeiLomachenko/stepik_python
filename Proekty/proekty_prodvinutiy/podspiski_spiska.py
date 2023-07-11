stroka = input()
stroka1 = stroka.split()
v = [[]]
dop = []
for i in range(len(stroka1)):
    for j in range(len(stroka1)):
        dop = stroka1[j:i + j + 1]
        if len(dop) == i + 1:
            v.append(dop)
print(v)