def i_in():
    return int(input())


def i_map():
    return map(int, input().split())


def solve():
    answer = 0
    x = list(input())
    t = x[0]
    x[0] = x[4]
    x[4] = t
    return "".join(x)


t = i_in()


for _ in range(t):
    print(solve())
