n = int(input())
c1 = 0
c2 = 0
c3 = 0
c4 = 0
for i in range(1, n + 1):
    x, y = map(int, input().split())
    if x > 0 and y > 0:
        c1 += 1
    elif x < 0 and y > 0:
        c2 += 1
    elif x < 0 and y < 0:
        c3 += 1
    elif x > 0 and y < 0:
        c4 += 1
print("Первая четверть:", c1)
print("Вторая четверть:", c2)
print("Третья четверть:", c3)
print("Четвертая четверть:", c4)
