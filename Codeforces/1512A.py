def solve():
    n = int(input())
    a = list(map(int, input().split(" ")))
    s = sorted([(a[i], i) for i in range(n)], key=lambda x: (x[0], x[1]))
    if s[0][0] != s[1][0]:
        return s[0][1] + 1
    return s[-1][1] + 1


t = int(input())


for _ in range(t):
    print(solve())
