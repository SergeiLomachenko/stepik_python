n1 = input().lower()
n2 = input().lower()
spisok = ['камень', 'ящерица', 'спок', 'ножницы', 'бумага']
if n1 in spisok:
    i1 = spisok.index(n1)
if n2 in spisok:
    i2 = spisok.index(n2)
if i1 == i2:
    print("ничья")
elif (i1 - i2) % 2 == 0:
    a1 = spisok[max(i1, i2)]
    if a1 == n1:
        print("Тимур")
    else:
        print("Руслан")
elif (i1 - i2) % 2 == 1:
    a2 = spisok[min(i1, i2)]
    if a2 == n1:
        print("Тимур")
    else:
        print("Руслан")