total = 0
for n in range(1, 151):
    for k in range(n, 151):
        for m in range(k, 151):
            for a in range(m, 151):
                for b in range(a, 151):
                    if n**5 + k**5 + m**5 + a**5 == b**5:
                        total += 1
                        print('n + k + m + a + b ==', m + k + n + a + b)
print(total)
