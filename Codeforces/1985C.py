def i_in():
    return int(input())


def i_map():
    return map(int, input().split())


def solve():
    answer = 0
    n = i_in()
    a = list(i_map())
    s = 0
    m = 0
    for i in range(n):
        s += a[i]
        if m < a[i]:
            m = a[i]
        if s - m == m:
            answer += 1
    return answer


t = i_in()


for _ in range(t):
    print(solve())
