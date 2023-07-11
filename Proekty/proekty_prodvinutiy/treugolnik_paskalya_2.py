n = int(input())
import math
for j in range(0, n):
    list = []
    for i in range(0, n):
        if j < i:
            break
        else:
            a=int(math.factorial(j)/(math.factorial(i)*math.factorial(j-i)))
            list.append(a)
    for k in range(len(list)):
        print(list[k], end = ' ')
    print()