def solve():
    a, b = map(lambda x: int(x), input().split(" "))
    if a == b:
        return 0
    df = abs(a - b)
    if df % 10 == 0:
        return df // 10
    else:
        return df // 10 + 1


t = int(input())


for _ in range(t):
    print(solve())
