def solve(lines):
    s = 0
    for line in lines:
        c = [i for i in line if i >= '0' and i <='9']
        if len(c) >= 2:
            s += int(f'{c[0]}{c[-1]}')
        else:
            s += int(f'{c[0]}{c[0]}')

    return s

with open('in', 'r') as f:
    lines = f.readlines()
    print(solve(lines))

