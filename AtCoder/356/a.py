def solve():
    answer = -1
    N, L, R = [int(i) for i in input().split(" ")]
    a = [i for i in range(1, N + 1)]
    a[L - 1 : R] = a[L - 1 : R][::-1]
    return " ".join([str(i) for i in a])


print(solve())
