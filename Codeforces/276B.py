from collections import Counter


def solve():
    x = input()
    d = Counter(x)
    c = 0
    if len(set(x)) == 1:
        return "First"
    for i in d:
        if d[i] % 2 != 0:
            c += 1
    if c == 0:
        return "First"
    if c % 2 != 0:
        return "First"
    else:
        return "Second"


print(solve())
