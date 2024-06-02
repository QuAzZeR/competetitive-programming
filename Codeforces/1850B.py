def i_in():
    return int(input())


def i_map():
    return map(int, input().split())


def solve():
    most = 0
    index = -1
    n = i_in()
    for i in range(n):
        a, b = i_map()
        if a <= 10 and b > most:
            most = b
            index = i

    return index + 1


t = i_in()


for _ in range(t):
    print(solve())
