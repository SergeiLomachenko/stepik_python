n, m = input().split()
matr = []
for i in range(int(n)):
    mi = []
    for j in range(int(m)):
        elem = int(m) * i + j + 1
        mi.append(elem)

        print(str(elem).ljust(3), end='')
    matr.append(mi)
    print()