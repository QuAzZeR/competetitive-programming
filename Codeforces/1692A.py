def i_in():
    return int(input())


def i_map():
    return map(int, input().split())


def solve():
    a = list(i_map())
    answer = 0
    for i in range(1, 4):
        if a[i] > a[0]:
            answer += 1
    return answer


t = i_in()


for _ in range(t):
    print(solve())
