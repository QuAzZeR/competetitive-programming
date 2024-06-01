def solve():
    N, M = [int(i) for i in input().split(" ")]
    a = [int(i) for i in input().split(" ")]
    answer = "No"
    for i in range(N):
        x = [int(i) for i in input().split(" ")]
        for i in range(M):
            a[i] -= x[i]

    for i in range(M):
        if a[i] > 0:
            return "No"
    return "Yes"


print(solve())
