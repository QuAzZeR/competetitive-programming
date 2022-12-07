with open('in', 'r') as f:
    rows = f.readlines()
    SUM = 0
    s = []
    for row in rows:
        x = row.strip()
        if x == '':
            s.append(SUM)
            SUM = 0
            continue
        SUM += int(x)
    print(sum(sorted(s, reverse=True)[0:3]))
