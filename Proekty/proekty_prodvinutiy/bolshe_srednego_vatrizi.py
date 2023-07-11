n = int(input())
matrix = []
matrixsum = []
for i in range(n):
    count = 0
    elem = [int(l) for l in input().split()]
    sumelem = 0
    for j in range(len(elem)):
        sumelem += elem[j]
    srednee = sumelem / len(elem)
    for k in range(len(elem)):
        if elem[k] > srednee:
            count +=1
    matrix.append(elem)
    print(count)
