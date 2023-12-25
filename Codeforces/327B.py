b = int(input())

def solve():
    for i in range(1,100):
        c = i**i
        if c == b:
            return i
        if c > b:
            return -1
    return -1

print(solve())
