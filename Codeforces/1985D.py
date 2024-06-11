def i_in():
    return int(input())


def i_map():
    return map(int, input().split())


def solve():
    answer = 0
    n, m = list(i_map())
    x, y = 1, 1
    mc = 0
    stop = False
    for i in range(n):
        a = input()
        if stop:
            continue
        c = a.count("#")
        if c == 0:
            continue
        if c < mc:
            stop = True
            continue
        cc = 0
        mc = c
        x = i + 1
        for j in range(m):
            if a[j] == "#":
                cc += 1
                if cc == c // 2 + 1:
                    y = j + 1
                    break
    return f"{x} {y}"


t = i_in()


for _ in range(t):
    print(solve())
