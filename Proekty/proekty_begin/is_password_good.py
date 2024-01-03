def is_password_good(password):
    count_ob = 0
    count1 = 0
    count2 = 0
    count3 = 0
    count4 = 0
    if len(password) >= 8:
        count1 += 1
    if password.lower() != password:
        count2 += 1
    if password.upper() != password:
        count3 += 1
    if password.isalnum() and not password.isalpha():
        count4 += 1
    count_ob = count1 + count2 + count3 + count4
    if count_ob == 4:
        return True
    else:
        return False
# считываем данные
txt = input()
# вызываем функцию
print(is_password_good(txt))