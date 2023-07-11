num = int(input())

def is_prime(num):
    delitel = 0
    for i in range(1, num + 1):
        if num % i == 0:
            delitel += 1
    if delitel > 2:
        return False
    if num < 2:
        return False
    else:
        return True                
while num > 0:
    num += 1
    is_prime(num)
    if is_prime(num) == True:
        print(num)  
        break