def solve():
    a, b, c = sorted([int(i) for i in input().split(" ")])
    return "Yes" if a + b == c else "No"


t = int(input())


for _ in range(t):
    print(solve())
