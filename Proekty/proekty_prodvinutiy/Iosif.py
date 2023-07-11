n = int(input())
k = int(input())
list = []
for i in range(1, n + 1):
    list.append(i)
while len(list) > 1:
    for j in range(1, k):
        temp = list.pop(0) #удаляем в начале
        list.append(temp) #добавляем в конец
    list.pop(0) #удаляем ( убиваем )
for m in range(len(list)):
    print(list[m])