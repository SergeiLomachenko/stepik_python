rows = 'abcdefgh'
columns = '87654321'
xy = input()
x = xy[0]
y = xy[1]
rows_ind = rows.index(x)
columns_ind = columns.index(y)
matr = []
for k in range(8):
    matr.append(['. '] * 8)
matr[columns_ind][rows_ind] = 'N '
for l in range(len(matr)):
    for h in range(len(matr)):
        if ((columns_ind - l)**2 + (rows_ind - h)**2 == 5):
            matr[l][h] = '* '
        print(matr[l][h], end = '')
    print()