n, m = input().split()

for i in range(int(n)):
    for j in range(int(m)):
        if (i + j) % 2 == 0:
            print(".", end = " ")
        else:
            print("*", end = " ")
    print()
