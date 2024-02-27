for a in range(1, 33):
    for b in range(a, 33):
        for c in range(b, 33):
            for d in range(c, 33):
                if (a ** 3 + b ** 3 == c ** 3 + d ** 3) and (a != b != c) and a != d and b != c and b != d and c != d:
                    kol = a ** 3 + b ** 3
                    print(kol)
