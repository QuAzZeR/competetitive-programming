def i_in():
    return int(input())


def i_map():
    return map(int, input().split())


def solve():
    answer = 0
    n = i_in()
    m = 0
    for i in range(2, n + 1):
        k = 1
        s = 0
        while k * i <= n:
            s += k * i
            k += 1
        if s > m:
            m = s
            answer = i

    return answer


t = i_in()


for _ in range(t):
    print(solve())
