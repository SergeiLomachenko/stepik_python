def is_valid_password(password):
    password = password.split(":")
    a = password[0]
    b = password[1]
    c = password[2]
    count = 0
    a1 = a[::-1]
    if a == a1:
        count += 1
    count2 = 1
    b = int(b)
    x = b + 1
    for i in range(2, x):
        if b % i == 0:
            count2 += 1
    if count2 == 2:
        count += 1
    c = int(c)
    if c % 2 == 0:
        count += 1
    if count == 3 and len(password) == 3:
        return True
    else:
        return False

# считываем данные
psw = input()

# вызываем функцию
print(is_valid_password(psw))