def solve():
    n = int(input())
    if n <= 2:
        return "NO"
    if n % 2 != 0:
        return "YES"
    for i in range(1, 60):
        power_2 = 2**i
        pair = n // power_2
        if power_2 > n:
            return "NO"
        if pair > 1 and pair % 2 != 0 and pair * power_2 == n:
            return "YES"
    return "NO"


t = int(input())


for i in range(t):
    print(solve())
