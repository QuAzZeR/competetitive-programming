with open('in', 'r') as f:
    rows = f.readlines()
    count = 0
    c = 0
    MIN = 0
    MAX = 0
    for i in range(len(rows)):
        row = rows[i].strip()
        # print(row, c)
        f,s = row.strip().split(',')
        f1,f2 = (int(i) for i in f.split('-'))
        s1,s2 = (int(i) for i in s.split('-'))
        if f2 >= s1 and f2 <= s2:
            count += 1
        elif s2 >= f1 and s2 <= f2:
            count += 1
    print(count)

