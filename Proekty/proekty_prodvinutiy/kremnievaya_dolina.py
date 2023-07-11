k = int(input())
holodilniki = []
for i in range(k):
    a = input()
    holodilniki.append(a)
spisok_holodilnikov_s_virusom = []
for j in range(len(holodilniki)):
            if 'a' in holodilniki[j]:
                l = holodilniki[j]
                f = holodilniki[j].find("a") + 1
                l = l[f:]
                if 'n' in l:
                    f = l.find("n") + 1
                    l = l[f:]
                    if 't' in l:
                        f = l.find("t") + 1
                        l = l[f:]
                        if 'o' in l:
                            f = l.find("o") + 1
                            l = l[f:]
                            if 'n' in l:
                                f = l.find("n") +1
                                l = l[f:]
                                spisok_holodilnikov_s_virusom.append(j + 1)
for n in range(len(spisok_holodilnikov_s_virusom)):
    print(spisok_holodilnikov_s_virusom[n], end = ' ')