alph = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
text = input('Введите текст для обработки:\n')
text2 = text.split(' ')
s = []
for j in range(len(text2)):
    b = text2[j]
    count1 = 0
    for k in range(len(b)):
        if b[k].isalpha():
            count1 += 1
    step = count1
    for i in range(len(b)):
        if b[i].isalpha():
            if b[i].islower():
                char = chr((ord(b[i]) - 97 + int(step)) % len(alph) + 97)
                s.append(char)

            if b[i].isupper():
                char = chr((ord(b[i]) - 65 + int(step)) % len(alph) + 65)
                s.append(char)

        else:
            s.append(b[i])
    s.append(' ')
for l in range(len(s)):
    print(s[l], end = '')