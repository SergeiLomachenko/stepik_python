n = int(input())
import math
list = []
for i in range(0, n + 1):
    a = math.comb(n, i)
    list.append(a)
print(list)