def i_in():
    return int(input())


def i_map():
    return map(int, input().split())


def solve():
    answer = 0
    a = list(i_map())
    a.sort()
    return "Yes" if a[1] + a[2] >= 10 else "No"


t = i_in()


for _ in range(t):
    print(solve())
