def convert_to_python_case(text):
    t2 = text.lower()
    l = len(text)
    t3 = [t2[0]]
    for i in range(1, l):
        if text[i] == t2[i]:
            t3.append(t2[i])
        else:
            t3.append('_')
            t3.append(t2[i])
    for j in range(len(t3)):
        print(t3[j], end = '')
# считываем данные
txt = input()

convert_to_python_case(txt)