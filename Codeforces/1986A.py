def i_in():
    return int(input())


def i_map():
    return map(int, input().split())


def solve():
    x = list(i_map())
    m = len(x)
    answer = 10000
    for a in range(max(x)+1):
        answer = min(answer, abs(a-x[0]) + abs(a-x[1]) + abs(a-x[2]))
    return answer


t = i_in()


for _ in range(t):
    print(solve())
