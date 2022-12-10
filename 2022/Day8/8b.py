m = []
with open('in', 'r') as f:
    rows = f.readlines()
    for row in rows:
        m.append([int(i) for i in row.strip()])
print(m)
l = len(m)
maximum_seen_tree = 0
def look_up(row,column):
    c =0
    for i in range(row-1, -1,-1):
        c+=1
        if m[i][column] >= m[row][column]:
            break
    return c

def look_down(row, column):
    c  = 0
    for i in range(row+1, l):
        c+=1
        if m[i][column] >= m[row][column]:
            break
    return c

def look_left(row, column):
    c = 0
    for i in range(column-1, -1, -1):
        c+=1
        if m[row][i] >= m[row][column]:
            break
    return c
def look_right(row, column):
    c = 0
    for i in range(column+1, len(m[0])):
        c+= 1
        if m[row][i] >= m[row][column]:
            break
    return c

for i in range(1, len(m[0])-1):
    for j in range(1, l-1):
        s = 1
        s *= look_up(i,j)
        s *= look_down(i,j)
        s *= look_left(i,j)
        s *= look_right(i,j)
        if s > maximum_seen_tree:
            maximum_seen_tree = s
        print(i,j,m[i][j],s, look_up(i,j), look_left(i,j),look_down(i,j), look_right(i,j),maximum_seen_tree)


print(maximum_seen_tree)
