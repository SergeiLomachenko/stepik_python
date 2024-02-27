n = int(input())
s = 0
while n >= 10:
    x = n % 10
    if x % 2 == 0:
        s = s + 1
    n //= 10
print(s)