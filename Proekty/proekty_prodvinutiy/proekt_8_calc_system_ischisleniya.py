n = int(input())
c1 = str(bin(n))
c1 = c1[2:]
c2 = str(oct(n))
c2 = c2[2:]
c3 = hex(n).upper()
c3 = c3[2:]
print(c1, c2, c3, sep = '\n')
