with open('in', 'r') as f:
    rows = f.readlines()
    s = 0
    for row in rows:
        text = row.strip()
        l = int(len(text)/2)
        first = text[:l]
        second = text[l:]
        t = {}
        for  i in first:
            if i not in t:
                t[i] = {1: 0, 2:0}
            t[i][1] += 1

        for  i in second:
            if i not in t:
                t[i] = {1: 0, 2:0}
            t[i][2] += 1
        for i in t :
            if t[i][2] != 0 and t[i][1] != 0:
                if i  >= 'A' and i <= 'Z':
                    s += ord(i) - 38
                if i >= 'a' and i <= 'z':
                    s += ord(i) - 96
                break
    print(s)

