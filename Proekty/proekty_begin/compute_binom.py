import math
def fact():
    k1 = math.factorial(n)
    k2 = math.factorial(k)
    k3 = n - k
    k4 = math.factorial(k3)
    return k1, k2, k4
def compute_binom(n, k):
    a, b, c = fact()
    n = a
    k = b * c
    return int(n / k)

# считываем данные
n = int(input())
k = int(input())

# вызываем функцию
print(compute_binom(n, k))