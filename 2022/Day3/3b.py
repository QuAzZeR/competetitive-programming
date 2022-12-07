with open('in', 'r') as f:
    rows = f.readlines()
    s = 0
    c = 0
    t = {}
    for i in range(len(rows)):
        c += 1
        text = rows[i].strip()
        for  i in text:
            if i not in t:
                t[i] = {1: 0, 2:0, 3:0}
            t[i][c] += 1
        if c == 3:
            for i in t :
                if t[i][2] != 0 and t[i][1] != 0 and t[i][3] != 0:
                    if i  >= 'A' and i <= 'Z':
                        s += ord(i) - 38
                    if i >= 'a' and i <= 'z':
                        s += ord(i) - 96
                    break
            t = {}
            c = 0
    print(s)

