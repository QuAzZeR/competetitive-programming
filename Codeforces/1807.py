def i_in():
    return int(input())


def i_map():
    return map(int, input().split())


def solve():
    answer = 0
    a, b, c = i_map()
    if a + b == c:
        return "+"
    if a - b == c:
        return "-"
    return answer


t = i_in()


for _ in range(t):
    print(solve())
