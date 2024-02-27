def chunked():
    stroka = input()
    stroka1= stroka.split()
    n = int(input())
    d = []
    for i in range(0, len(stroka1), n):
        d.append(stroka1[i:(i + n)])
    print(d)
chunked()