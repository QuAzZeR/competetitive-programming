with open('in', 'r') as f:
    rows = f.readlines()
    is_get = True
    m = {}
    index = {
    }
    position = {}
    for i in range(len(rows)):
        text = rows[i].replace('\n', '')
        if 'move' in text:
            # start moving here
            s = text .split(' ')
            c = int(s[1])
            f = s[3]
            t = s[5]
            for j in range(index[f]-c, index[f]):
                m[t][index[t]] = m[f][j]
                del m[f][j]
                index[t] += 1
            index[f] -= c
            continue
        elif ' 1' in text:
            for j in range(len(text)):
                if text[j] not in ['', ' ']:
                    position[text[j]] = j
                    index[text[j]] = 0
            for j in range(i-1, -1, -1):
                t = rows[j].replace('\n', '')
                for k in position:
                    if k not in m:
                        m[k] = {}
                    if t[position[k]] not in ['', ' ']:
                        m[k][index[k]] = t[position[k]]
                        index[k] += 1

answer = ''
for i in range(1, len(index) + 1):
    str_i = str(i)
    answer += m[str_i][index[str_i]-1]
print(answer)
