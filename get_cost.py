def get_shipping_cost(quantity):
    s = 1000 + (quantity - 1) * 120
    return s
n = int(input())
print(get_shipping_cost(n))