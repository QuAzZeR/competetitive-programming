def i_in():
    return int(input())


def i_map():
    return map(int, input().split())


def solve():
    answer = 0
    n, f, k = i_map()
    a = list(i_map())
    v = a[f - 1]
    a.sort(reverse=True)
    if v in a[0:k] and v in a[k:]:
        return "MAYBE"
    elif v in a[0:k]:
        return "YES"
    elif v in a[k:]:
        return "NO"


t = i_in()


for _ in range(t):
    print(solve())
