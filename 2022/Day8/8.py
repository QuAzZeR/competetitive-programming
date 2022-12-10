m = []
with open('in', 'r') as f:
    rows = f.readlines()
    for row in rows:
        m.append([int(i) for i in row.strip()])
print(m)
l = len(m)
answer = l*2 + (l-2)*2

def look_up(row,column):
    for i in range(row-1, -1,-1):
        if m[i][column] >= m[row][column]:
            return  False
    return True

def look_down(row, column):
    for i in range(row+1, l):
        if m[i][column] >= m[row][column]:
            return  False
    return True

def look_left(row, column):
    for i in range(column-1, -1, -1):
        if m[row][i] >= m[row][column]:
            return  False
    return True
def look_right(row, column):
    for i in range(column+1, len(m[0])):
        if m[row][i] >= m[row][column]:
            return  False
    return True

for i in range(1, len(m[0])-1):
    for j in range(1, l-1):
        s = False
        s = s or look_up(i,j)
        s = s or look_down(i,j)
        s = s or look_left(i,j)
        s = s or look_right(i,j)
        if s == True:
            answer += 1
        # print(i,j,m[i][j],s, answer)


print(answer)
