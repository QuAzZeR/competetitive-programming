def i_in():
    return int(input())


def i_map():
    return map(int, input().split())


def solve():
    n = i_in()
    a = list(i_map())
    b = list(i_map())
    m = i_in()
    d = list(i_map())
    found = {}
    for i in range(n):
        if a[i] != b[i]:
            if b[i] not in found:
                found[b[i]] = 0
            found[b[i]] += 1
    if d[-1] not in b:
        return "NO"
    q = 0
    for i in d:
        if i in found:
            found[i] = max(0, found[i] - 1)
    for i in found:
        q += found[i]
    if q != 0:
        return "NO"

    return "YES"


t = i_in()


for _ in range(t):
    print(solve())
